from django.shortcuts import render

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .serializers import CostumerSerializer, CostumerCreateSerializer, MotorcycleCreateSerializer, MotorcycleSerializer
from .models import Costumer, Motorcycle

class CostumerCreateList(APIView):

    def get(self, request):
        costumers = Costumer.objects.all()
        if not costumers:
            raise APIException('Não existem clientes cadastrados')
        
        serializer = CostumerSerializer(costumers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CostumerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CostumerDeleteUpdate(APIView):

    def get_object(self, pk):

        try:
            return Costumer.objects.get(pk=pk)
        except Costumer.DoesNotExist:
            return None
        
    def get(self, request, pk):
        costumer = self.get_object(pk)
        if costumer is None:
            return Response({"erro": 'não existem cliente com esse id'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CostumerSerializer(costumer)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        costumer = self.get_object(pk)
        if costumer is None:
            return Response({"erro": 'não existem cliente com esse id'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CostumerCreateSerializer(costumer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        costumer = self.get_object(pk)
        if costumer is None:
            return Response({"erro": 'não existem cliente com esse id'}, status=status.HTTP_404_NOT_FOUND)
        costumer.delete()
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
