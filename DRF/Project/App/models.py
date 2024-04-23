from django.db import models

# Create your models here.

class FoodItemModel(models.Model):
    Item_Name = models.CharField(max_length=100)
    Item_Price = models.IntegerField()
    Item_Qty = models.IntegerField()
    Item_Desc = models.CharField(max_length=250)
    def __str__(self):
        return str(self.Item_Name)
    class Meta():
        pass