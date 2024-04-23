from rest_framework import serializers
from .models import *

class ListSerializer(serializers.ModelSerializer):
    class Meta():
        model = ListModel
        fields = '__all__'