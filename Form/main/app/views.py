from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def Registration(request):
    if request.method == 'POST':
        Names = request.POST.get('name')
        Emails = request.POST.get('email')
        Passwords = request.POST.get('password')
        data={
            Names:'Names',
            Emails:Emails,
            Passwords:Passwords
        }
        okay = InfoModel.objects.create(Name=Names,Email=Emails,Password=Passwords)
    return HttpResponse('Data Saved')