from django import forms 
from .models import *

class StudentForm(forms.ModelForm):
    class Meta():
        model = InfoModel
        fields = "__all__"
    