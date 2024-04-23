from django.db import models

# Create your models here.
class NewsModel(models.Model):
    news = models.CharField(max_length=255)
    newsInfo = models.CharField(max_length=255)

class StudentDetails(models.Model):
    Name = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Email = models.EmailField()
    Contact = models.IntegerField()
    def __str__(self):
        return str(self.Name)