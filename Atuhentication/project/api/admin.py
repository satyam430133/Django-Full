from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(MovieModel)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city']
# admin.site.register(MovieModel)

@admin.register(ArtStudentModel)
class ArtStudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city']

@admin.register(BioStudentModel)
class BioStudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city']

@admin.register(MathStudentModel)
class MathStudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city']
