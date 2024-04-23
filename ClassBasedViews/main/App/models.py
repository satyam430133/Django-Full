from django.db import models

# Create your models here.
class MovieModel(models.Model):
    Name = models.CharField(max_length=100)
    ReleaseDate = models.IntegerField()
    Rating = models.CharField(max_length=50)
    Desc = models.CharField(max_length=250)
    class Meta():
        pass