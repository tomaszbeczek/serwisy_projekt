from django.db import models

# Create your models here.

class Car(models.Model):
    vehicle_brand = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=13)


