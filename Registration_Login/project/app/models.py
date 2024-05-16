from django.db import models

# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_Number = models.IntegerField()
    Password = models.CharField(max_length=100)
    Confirm_Password = models.CharField(max_length=100)
    class Meta():
        verbose_name_plural = 'UserList'
    def __str__(self):
        return str(self.Name)