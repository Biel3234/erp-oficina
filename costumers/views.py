from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException


from .serializers import CostumerSerializer
from .models import Costumer 

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
    

