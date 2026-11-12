from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PartSerializer, CategorySerializer, MovementSerializer
from .models import Part, Category, Movement
from .services import register_movement

from rest_framework.permissions import IsAuthenticated
# Part CRUD

class PartListCreate(ListCreateAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()

class PartDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PartSerializer
    queryset = Part.objects.all()

# Category CRUD

class CategoryListCreate(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

# Movement CRUD

class MovementListCreate(ListCreateAPIView):
    serializer_class = MovementSerializer
    queryset = Movement.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        movement = register_movement(
            movement_type=serializer.validated_data['movement_type'],
            part_id=serializer.validated_data['part'].id,
            quantity=serializer.validated_data['quantity'],
            created_by = request.user,
        )

        response_serializer = self.get_serializer(movement)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )

class MovementDetail(RetrieveAPIView):
    serializer_class = MovementSerializer
    queryset = Movement.objects.all()