from django.db import models

# Create your models here.

class Car(models.Model):
    vehicle_brand = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=13)
    max_tank = models.IntegerField(max_length=2)
    available = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete = models.SET_NULL,null = True)
    rent = models.CharField(max_length=10, blank = True)



class Location(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city




