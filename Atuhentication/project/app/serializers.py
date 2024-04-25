from rest_framework import serializers
from .models import StuModel

class StuSrlzr(serializers.ModelSerializer):
    class Meta():
        model = StuModel
        fields = '__all__'