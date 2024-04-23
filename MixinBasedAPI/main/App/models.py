from django.db import models

# Create your models here.

class StudentModel(models.Model):
    Name =  models.CharField(max_length=50)
    Class = models.IntegerField()
    Subject = models.CharField(max_length=100)
    class Meta():
        pass