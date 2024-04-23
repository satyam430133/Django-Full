from rest_framework import serializers
from .models import *

class MovieSerializers(serializers.ModelSerializer):
    class Meta():
        model = MovieModel
        fields = "__all__"