from .models import Costumer, Motorcycle
from rest_framework import serializers

class MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ['id','model', 'color', 'license_plate', 'owner']

class MotorcycleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ['model', 'color', 'license_plate', 'owner']

    
class CostumerSerializer(serializers.ModelSerializer):
    motorcycle = MotorcycleSerializer(read_only=True)
    class Meta:
        model = Costumer
        fields = ['id', 'name', 'phone', 'motorcycle']

class CostumerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = ['name', 'phone', 'motorcycle']
    