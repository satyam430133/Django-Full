from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(AdharModel)
# admin.site.register(StudentModel)

@admin.register(AdharModel)
class AdharAdmin(admin.ModelAdmin):
    list_display=['id','aadhar_no']

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['stu_name','aadhar_no']