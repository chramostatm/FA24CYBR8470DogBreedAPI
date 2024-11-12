from rest_framework import serializers
from .models import Dog
from .models import Breeds

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'age', 'breed','owner']

class BreedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breeds
        fields = ['id', 'name', 'age', 'breed','owner']