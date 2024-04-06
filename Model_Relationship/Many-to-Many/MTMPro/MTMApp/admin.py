from django.contrib import admin
from .models import *
# Register your models here.

# class Student(admin.ModelAdmin):
#     list_display = '__all__'
# admin.site.register(FuelTypeModel)
# admin.site.register(CarModel)

class Fuel(admin.ModelAdmin):
    list_display=['id','fuelName']
admin.site.register(FuelTypeModel,Fuel)

class Car(admin.ModelAdmin):
    list_display=['id','carName']
admin.site.register(CarModel,Car)