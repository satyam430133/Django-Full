from django.db import models

# Create your models here.
Fuel = [
    ('petrol','petrol'),
    ('diesel','diesel'),
    ('CNG','CNG'),
    ('LPG','LPG'),
]
class FuelTypeModel(models.Model):
    fuelName = models.CharField(max_length=100,choices=Fuel)
    def __str__(self):
        return str(self.fuelName)

Car = [
    ('tata','tata'),
    ('volvo','volvo'),
    ('honda','honda'),
    ('BMW','BMW'),
    ('swift','swift'),
]
class CarModel(models.Model):
    carName = models.CharField(max_length=100,choices=Car)
    fuelName = models.ManyToManyField(FuelTypeModel)
    def __str__(self):
        return str(self.carName)