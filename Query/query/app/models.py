from django.db import models

# Create your models here.
class NewsModel(models.Model):
    news = models.CharField(max_length=255)
    newsInfo = models.CharField(max_length=255)