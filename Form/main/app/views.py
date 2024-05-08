from django.shortcuts import render,HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def Registration(request):
   try:
        if request.method == 'POST':
            Names = request.POST.get('name')
            Emails = request.POST.get('email')
            Passwords = request.POST.get('password')
            if Names and Emails and Passwords != '':
                fill = InfoModel.objects.filter(Email = Emails)
                if fill:
                    msg = "already registered"
                    return render(request, 'index.html',{'key':msg})
                else:
                    msg = "Data Saved"
                    okay = InfoModel.objects.create(Name=Names,Email=Emails,Password=Passwords)
                    return render(request, 'index.html',{'key':msg})
                msg = "Please Fill Details"
                return render(request, 'index.html',{'key':msg})
            else:
                return render(request, 'index.html')
   except:
        msg = "Code Error"
        return render(request, 'index.html',{'key':msg})