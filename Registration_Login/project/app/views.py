from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import *
# Create your views here.

def home(request):
    return render(request,'index.html')

def Registration(request):
    if request.method == 'POST':
        unames = request.POST.get('username')
        emails = request.POST.get('email')
        phones = request.POST.get('phone')
        passwords = request.POST.get('password')
        cpass = request.POST.get('confirm_password')
        userdata = User.objects.filter(Email=emails)
        if userdata:
            msg = 'User Already Exist Login'
            return render(request,'login.html',{'key':msg})
        else:
            if passwords == cpass:
                User.objects.create(Name=unames,Email=emails,Phone_Number=phones,Password=passwords,Confirm_Password=cpass)
                msg = "Registration Successfull"
                return render(request,'login.html',{'key':msg})
            msg = 'Password & Confirm Password Does Not Match'
            return render(request,'registration.html',{'key':msg})
        return render(request,'registration.html')
    else:
        return render(request,'registration.html')

def Login(request):
    if request.method == 'POST':
        loginemail = request.POST.get('login_email')
        loginpass = request.POST.get('login_password')
        userdata = User.objects.get(Email=loginemail)
        if userdata.Email == loginemail:
            user = User.objects.get(Email=loginemail)
            alluser = User.objects.all()
            msg = 'Login Successfull'
            return render(request,'index.html',{'key':msg,'user':user,'alluser':alluser})
        else:
            msg = 'Not A User Register First'
            return redirect('register',{'key':msg}) 
    return render(request,'login.html')