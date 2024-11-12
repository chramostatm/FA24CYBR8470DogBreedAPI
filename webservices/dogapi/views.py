from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import DogSerializer
from .serializers import BreedSerializer
from .models import Dog
from .models import Breed
# Create your views here.
#ViewSets https://www.django-rest-framework.org/api-guide/viewsets/
class DogViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Dog.objects.all()
        serializer = DogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Dog.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(user)
        return Response(serializer.data)
    
    def add(self, request, pk=None):
        queryset = Dog.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(user)
        return Response(serializer.data)
    
    def remove(self, request, pk=None):
        queryset = Dog.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(user)
        return Response(serializer.data)
    
class BreedViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Breed.objects.all()
        serializer = BreedSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Breed.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BreedSerializer(user)
        return Response(serializer.data)
    
    def add(self, request, pk=None):
        queryset = Dog.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(user)
        return Response(serializer.data)
    
    def remove(self, request, pk=None):
        queryset = Dog.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(user)
        return Response(serializer.data)
