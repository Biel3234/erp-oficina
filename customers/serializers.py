from .models import Customer, Motorcycle
from rest_framework import serializers

class MotorcycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ['id','model', 'color', 'license_plate', 'owner']

class MotorcycleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorcycle
        fields = ['model', 'color', 'license_plate', 'owner']

    
class CustomerSerializer(serializers.ModelSerializer):
    motorcycle = MotorcycleSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'motorcycle']

class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'motorcycle']
    