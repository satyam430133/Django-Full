from django.db import models

class AdharModel(models.Model):
    aadhar_no = models.IntegerField()
    def __str__(self):
        return str(self.aadhar_no)
    
class StudentModel(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_address = models.CharField(max_length=100)

    # aadhar_no = models.OneToOneField(AdharModel,
    # on_delete=models.PROTECT,primary_key=True)

    aadhar_no = models.OneToOneField(AdharModel,
    on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return str(self.aadhar_no)