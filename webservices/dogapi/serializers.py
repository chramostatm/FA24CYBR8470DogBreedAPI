from rest_framework import serializers
from .models import Dog
from .models import Breed

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed','owner']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name', 'age', 'breed','owner']