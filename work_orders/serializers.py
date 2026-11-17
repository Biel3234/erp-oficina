from rest_framework import serializers
from .models import WorkOrder

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_by']
        model = WorkOrder