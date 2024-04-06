from django.shortcuts import render
from django.shortcuts import HttpResponse,render
from .models import *

# Create your views here.
def home(request):
    newss = NewsModel.objects.all()
    return render(request,'index.html',{'newss':newss})
