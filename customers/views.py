from django.shortcuts import render

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .serializers import CustomerSerializer, CustomerCreateSerializer, MotorcycleCreateSerializer, MotorcycleSerializer
from .models import Customer, Motorcycle

class CustomerCreateList(APIView):

    def get(self, request):
        customers = Customer.objects.all()
        if not customers:
            raise APIException('Não existem clientes cadastrados')
        
        serializer = CustomerSerializer(customers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDeleteUpdate(APIView):

    def get_object(self, pk):

        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return None
        
    def get(self, request, pk):
        customer = self.get_object(pk)
        if customer is None:
            return Response({"erro": 'não existem cliente com esse id'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(customer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        customer = self.get_object(pk)
        if customer is None:
            return Response({"erro": 'não existem cliente com esse id'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerCreateSerializer(customer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        if customer is None:
            return Response({"erro": 'não existem cliente com esse id'}, status=status.HTTP_404_NOT_FOUND)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MotorcycleCreateList(APIView):

    def get(self, request):
        motorcycles = Motorcycle.objects.all()
        if not motorcycles:
            raise APIException('Não existem motos cadastrados')
        
        serializer = MotorcycleSerializer(motorcycles, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MotorcycleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MotorcycleDeleteUpdate(APIView):

    def get_object(self, pk):

        try:
            return Motorcycle.objects.get(pk=pk)
        except Motorcycle.DoesNotExist:
            return None

    def get(self, request, pk):
        motorcycle = self.get_object(pk)
        if motorcycle is None:
            return Response({"erro": 'não existe moto com esse id'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MotorcycleSerializer(motorcycle)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        motorcycle = self.get_object(pk)
        if motorcycle is None:
            return Response({"erro": 'não existe moto com esse id'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MotorcycleCreateSerializer(motorcycle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        motorcycle = self.get_object(pk)
        if motorcycle is None:
            return Response({"erro": 'não existe moto com esse id'}, status=status.HTTP_404_NOT_FOUND)
        motorcycle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
