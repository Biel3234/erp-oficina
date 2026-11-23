from django.db import transaction
from rest_framework import serializers

from .models import PartWorkOrder, WorkOrder, WorkOrderParts
from .services import return_items_to_stock, take_items_from_stock

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'customer',
            'motorcycle',
            'reported_problem',
            'diagnosis',
            'labor_cost',
            'parts_cost',
            'status',
            'priority',
            'created_at',
            'updated_at',
            'created_by',
        ]
        read_only_fields = ['id', 'customer', 'parts_cost', 'created_by', 'created_at', 'updated_at']
        model = WorkOrder

class PartWorkOrderSerializer(serializers.ModelSerializer):
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    total = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = PartWorkOrder
        fields = ['id', 'part', 'quantity', 'unit_price', 'total']


class WorkOrderPartsSerializer(serializers.ModelSerializer):
    items = PartWorkOrderSerializer(many=True, required=False)

    class Meta:
        fields = ['id', 'workorder', 'items']
        model = WorkOrderParts

    def _user(self):
        request = self.context.get('request')
        return getattr(request, 'user', None)

    def _save_items(self, instance, items):
        created = PartWorkOrder.objects.bulk_create([
            PartWorkOrder(
                work_order_parts=instance,
                part=item['part'],
                quantity=item.get('quantity', 1),
                unit_price=item.get('unit_price', item['part'].price),
            )
            
            for item in items
        ])
        take_items_from_stock(created, self._user())

    @transaction.atomic
    def create(self, validated_data):
        items = validated_data.pop('items', [])
        instance = WorkOrderParts.objects.create(**validated_data)
        self._save_items(instance, items)
        if instance.workorder:
            instance.workorder.update_parts_cost()
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        items = validated_data.pop('items', None)
        old_workorder = instance.workorder
        instance = super().update(instance, validated_data)
        if items is not None:
            return_items_to_stock(instance.items.all(), self._user())
            instance.items.all().delete()
            self._save_items(instance, items)
        if old_workorder and old_workorder != instance.workorder:
            old_workorder.update_parts_cost()
        if instance.workorder:
            instance.workorder.update_parts_cost()
        return instance