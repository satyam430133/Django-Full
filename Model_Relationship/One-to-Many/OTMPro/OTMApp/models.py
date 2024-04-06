from django.db import models

# Create your models here.
class DepartmentModel(models.Model):
    depName = models.CharField(max_length=100,verbose_name='Name')
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.depName)

class StudentsModel(models.Model):
    StuName = models.CharField(max_length=50,verbose_name='Name')
    stuDep = models.ForeignKey(DepartmentModel,on_delete=models.PROTECT,null=True)
    def __str__(self):
        return str(self.StuName)