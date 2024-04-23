from rest_framework import serializers
from .models import *
class FoodSerializer(serializers.ModelSerializer):
    class Meta():
        model = FoodItemModel
        fields = "__all__"