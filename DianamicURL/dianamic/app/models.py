from django.db import models

# Create your models here.
class Student(models.Model):
    Names = models.CharField(max_length=50)
    Email = models.EmailField()
    Age = models.IntegerField(null=True)
    Phone = models.IntegerField()
    Address = models.CharField(max_length=50)
    class Meta:
        ordering = ['Names']
        # verbose_name = "jerry"
        # verbose_name + 'es'
        # verbose_name_plural = "ram"
        db_table = 'My_Students_List'