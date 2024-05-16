from django.shortcuts import render,redirect
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
        emails = request.POST.get('login_email')
        loginpass = request.POST.get('login_password')
        userdata = User.objects.get(Email=emails)
        if userdata.Email == emails:
            user = User.objects.get(Email=emails)
            alluser = User.objects.all()
            msg = 'Login Successfull'
            return render(request,'index.html',{'key':msg,'user':user,'alluser':alluser})
        else:
            msg = 'Not A User Register First'
            return redirect('register',{'key':msg}) 
    return render(request,'login.html')

def AddQuery(request,pk):
    user = User.objects.get(id=pk)
    return render(request,'queryform.html',{'user':user})

def SubmitQuery(request,pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        titles = request.POST.get('title')
        descriptions = request.POST.get('description')
        emails = request.POST.get('email')
        QueryModel.objects.create(Title=titles,Desc=descriptions,Email=user.Email)
        msg = 'Query Added'
        userdata = User.objects.get(Email=emails)
        if userdata.Email == emails:
            user = User.objects.get(Email=emails)
            alluser = User.objects.all()
            msg = 'Login Successfull'
            return render(request,'index.html',{'key':msg,'user':user,'alluser':alluser})
        return render(request,'index.html',{'key':msg})
    
def Show(request,pk):
    print(pk)
    showuser = QueryModel.objects.filter(Email=pk)
    return render(request,'show.html',{'showuser':showuser})