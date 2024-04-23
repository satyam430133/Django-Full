from django.db import models

# Create your models here.

class ListModel(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    class Meta():
        verbose_name_plural = 'ListModel'
    def __str__(self):
            str(self.Name)