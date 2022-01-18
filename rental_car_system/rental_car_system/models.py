from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *


# Create your models here.

class Car(models.Model):
    vehicle_brand = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=13)
    max_tank = models.IntegerField(max_length=2)
    available = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    rent = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.vehicle_brand + " " + self.vehicle_model


class Car_Dealer(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(10)], max_length=10)
    location = models.OneToOneField(Location, on_delete=models.PROTECT)
    profits = models.IntegerField(default=0)
    type = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.name)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(10)], max_length=10)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.user)


class Location(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_dealer = models.ForeignKey(Car_Dealer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rent = models.CharField(max_length=10)
    days = models.CharField(max_length=3)
    is_complete = models.BooleanField(default=False)

