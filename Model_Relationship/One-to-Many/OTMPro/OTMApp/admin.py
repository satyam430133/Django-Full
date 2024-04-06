from django.contrib import admin
from .models import *

# Register your models here.
class Student(admin.ModelAdmin):
    # list_display=['depName','description']
    list_display = '__all__'
admin.site.register(DepartmentModel)
admin.site.register(StudentsModel)
