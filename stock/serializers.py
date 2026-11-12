from rest_framework import serializers
from .models import Part, Category, Movement

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = Category
            fields = '__all__'

class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = '__all__'
        read_only_fields = ['created_at', 'created_by']

        def validate(self, data):
             if data.get('quantity_in_stock') < 0:
                  raise serializers.ValidationError(
                    {
                        'Estoque não pode ser negativo'
                    }
                  )
             return data