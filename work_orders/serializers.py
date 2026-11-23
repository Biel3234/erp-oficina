from django.db import transaction
from rest_framework import serializers

from .models import PartWorkOrder, WorkOrder, WorkOrderParts

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
        read_only_fields = ['id', 'customer', 'created_by', 'created_at', 'updated_at']
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

    def _save_items(self, instance, items):
        PartWorkOrder.objects.bulk_create([
            PartWorkOrder(
                work_order_parts=instance,
                part=item['part'],
                quantity=item.get('quantity', 1),
                unit_price=item.get('unit_price', item['part'].price),
            )
            for item in items
        ])

    @transaction.atomic
    def create(self, validated_data):
        items = validated_data.pop('items', [])
        instance = WorkOrderParts.objects.create(**validated_data)
        self._save_items(instance, items)
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        items = validated_data.pop('items', None)
        instance = super().update(instance, validated_data)
        if items is not None:
            instance.items.all().delete()
            self._save_items(instance, items)
        return instance