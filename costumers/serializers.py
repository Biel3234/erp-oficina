from .models import Costumer, Motorcycle
from rest_framework import serializers

class MotorcycleSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ['model', 'color', 'license_plate']
    

class CostumerSerializer(serializers.ModelSerializer):
    motorcycle = MotorcycleSimpleSerializer(read_only=True)
    class Meta:
        model = Costumer
        fields = ['id', 'name', 'phone', 'motorcycle']

class CostumerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = ['name', 'phone', 'motorcycle']
    