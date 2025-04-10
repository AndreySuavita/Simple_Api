from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MiModelo
from .serializers import MiModeloSerializer

class MiModeloListView(APIView):
    def get(self, request):
        objetos = MiModelo.objects.all()
        serializer = MiModeloSerializer(objetos, many=True)
        return Response(serializer.data)
    
class MiModeloCreateView(APIView):
    def post(self, request):
        serializer = MiModeloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MiModeloDeleteView(APIView):
    def delete(self, request, pk):
        try:
            objeto = MiModelo.objects.get(pk=pk)
            objeto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MiModelo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class MiModeloUpdateView(APIView):
    # put replace all the object
    def put(self, request, pk):
        try:
            objeto = MiModelo.objects.get(pk=pk)
        except MiModelo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MiModeloSerializer(objeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # patch replace only specific fields
    def patch(self, request, pk):
        try:
            objeto = MiModelo.objects.get(pk=pk)
        except MiModelo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = MiModeloSerializer(objeto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)