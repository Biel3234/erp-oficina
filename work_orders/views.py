from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import WorkOrder
from .serializers import WorkOrderSerializer


class WorkOrderCreateList(ListCreateAPIView):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer = serializer.save(created_by = self.request.user)

class WorkOrderDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = WorkOrderSerializer
    queryset = WorkOrder.objects.all()