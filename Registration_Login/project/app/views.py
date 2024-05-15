from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def home(request):
    return render(request,'index.html')

def Registration(request):
    return render(request,'registration.html')

def Login(request):
    return render(request,'login.html')