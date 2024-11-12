from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import DogSerializer
from .serializers import BreedSerializer
from .models import Dog
from .models import Breed
# Create your views here.
#ViewSets based on https://www.django-rest-framework.org/api-guide/viewsets/
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
        dog = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        Dog.objects.create(request)
        return Response(status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = Dog.objects.all()
        try:
            dog = get_object_or_404(queryset, pk=pk)
            Dog.objects.delete(dog)
        except:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
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
        breed = get_object_or_404(queryset, pk=pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)
    
    def update(self, request):
        Breed.objects.create(request)
        return Response(status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        queryset = Breed.objects.all()
        try:
            breed = get_object_or_404(queryset, pk=pk)
            Breed.objects.delete(Breed)
        except:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
    

