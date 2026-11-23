from django.db import transaction
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import WorkOrder, WorkOrderParts
from .serializers import WorkOrderPartsSerializer, WorkOrderSerializer
from .services import return_items_to_stock


class WorkOrderCreateList(ListCreateAPIView):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()

    def perform_create(self, serializer):
        motorcycle = serializer.validated_data['motorcycle']
        workorder = serializer.save(
            created_by=self.request.user,
            customer=motorcycle.owner,
        )
        WorkOrderParts.objects.create(workorder=workorder)

class WorkOrderDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()

class WorkOrderPartsCreateList(ListCreateAPIView):
    serializer_class = WorkOrderPartsSerializer
    queryset = WorkOrderParts.objects.select_related('workorder').prefetch_related('items')


class WorkOrderPartsDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = WorkOrderPartsSerializer
    queryset = WorkOrderParts.objects.select_related('workorder').prefetch_related('items')

    @transaction.atomic
    def perform_destroy(self, instance):
        workorder = instance.workorder
        return_items_to_stock(instance.items.all(), self.request.user)
        instance.delete()
        if workorder:
            workorder.update_parts_cost()