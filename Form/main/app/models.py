from django.db import models

# Create your models here.

class InfoModel(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    def __str__(self):
        return str(self.Name)