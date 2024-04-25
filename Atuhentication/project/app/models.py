from django.db import models
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your models here.
class StuModel(models.Model):
    permission_classes = [AllowAny]
    Name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.Name)