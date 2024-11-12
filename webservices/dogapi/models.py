from django.db import models
#Choices
# https://docs.djangoproject.com/en/5.0/ref/models/fields/#enumeration-types
SIZE_CHOICES = [
    ("T", "Tiny"),
    ("S", "Small"),
    ("M","Medium"),
    ("L","Large"),
]
Gender = [
    ("M","Male"),
    ("F","Female"),
    ("U","Unknown"),
]

get_scale= [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
]

# Create your models here.
#Breed Model
class Breed(models.Model):
    name= models.CharField(max_length=100)
    size = models.CharField(max_length=100,choices=SIZE_CHOICES)
    friendliness =models.IntegerField(choices=get_scale)
    trainability =models.IntegerField(choices=get_scale)
    sheedingamount =models.IntegerField(choices=get_scale)
    exerciseneeds =models.IntegerField(choices=get_scale)
    def __str__(self):
        return self.name
#Dog Model
class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed,on_delete=models.CASCADE, null=True, blank=True)
    gender =models.CharField(max_length=100, choices=Gender)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)
    def __str__(self):
        return self.name


