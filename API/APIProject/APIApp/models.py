from django.db import models

# Create your models here.
class StudentModel(models.Model):
    Name = models.CharField(max_length=100)
    Class = models.IntegerField()
    Subject = models.CharField(max_length=100)
    def __str__(self):
        return str(self.Name)