from django.shortcuts import render, redirect
from .models import User, QueryModel

def home(request):
    return render(request, 'index.html')

def Registration(request):
    if request.method == 'POST':
        unames = request.POST.get('username')
        pk = request.POST.get('email')
        phones = request.POST.get('phone')
        passwords = request.POST.get('password')
        cpass = request.POST.get('confirm_password')
        userdata = User.objects.filter(Email=pk)
        if userdata.exists():
            msg = 'User Already Exist. Login'
            return render(request, 'login.html', {'key': msg})
        else:
            if passwords == cpass:
                User.objects.create(Name=unames, Email=pk, Phone_Number=phones, Password=passwords, Confirm_Password=cpass)
                msg = "Registration Successful"
                return render(request, 'login.html', {'key': msg})
            msg = 'Password & Confirm Password Do Not Match'
            return render(request, 'registration.html', {'key': msg})
    return render(request, 'registration.html')

def Login(request):
    if request.method == 'POST':
        pk = request.POST.get('login_email')
        loginpass = request.POST.get('login_password')
        try:
            userdata = User.objects.get(Email=pk)
            if userdata.Password == loginpass:
                alluser = User.objects.all()
                msg = 'Login Successful'
                return render(request, 'index.html', {'key': msg, 'user': userdata, 'alluser': alluser})
            else:
                msg = 'Incorrect Password'
                return render(request, 'login.html', {'key': msg})
        except User.DoesNotExist:
            msg = 'Not A User. Register First'
            return render(request, 'registration.html', {'key': msg})
    return render(request, 'login.html')

def AddQuery(request, pk):
    queryuser = User.objects.filter(Email=pk)
    userdata = User.objects.get(Email=pk)
    alluser = User.objects.all()
    return render(request, 'index.html', {'user': userdata, 'alluser': alluser, 'queryuser': queryuser})

def SubmitQuery(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        titles = request.POST.get('title')
        descriptions = request.POST.get('description')
        QueryModel.objects.create(Title=titles, Desc=descriptions, Email=user.Email)
        msg = 'Query Added'
        alluser = User.objects.all()
        return render(request, 'index.html', {'user': user, 'alluser': alluser, 'key': msg})

def Show(request, pk):
    showuser = QueryModel.objects.filter(Email=pk)
    userdata = User.objects.get(Email=pk)
    alluser = User.objects.all()
    return render(request, 'index.html', {'user': userdata, 'alluser': alluser, 'showuser': showuser})

def EditQuery(request, pk):
    editdata = QueryModel.objects.get(id=pk)
    userdata = User.objects.get(Email=editdata.Email)
    alluser = User.objects.all()
    return render(request, 'index.html', {'user': userdata, 'alluser': alluser, 'editdata': editdata})

def UpdateData(request, pk):
    query = QueryModel.objects.get(id=pk)
    if request.method == 'POST':
        query.Title = request.POST.get('title')
        query.Desc = request.POST.get('description')
        query.save()
        msg = 'Query Updated'
        showuser = QueryModel.objects.filter(Email=query.Email)
        userdata = User.objects.get(Email=query.Email)
        alluser = User.objects.all()
        return render(request, 'index.html', {'key': msg, 'user': userdata, 'alluser': alluser, 'showuser': showuser})

def DeleteQuery(request, pk, ml):
    query = QueryModel.objects.get(id=pk)
    query.delete()
    showuser = QueryModel.objects.filter(Email=ml)
    userdata = User.objects.get(Email=ml)
    alluser = User.objects.all()
    return render(request, 'index.html', {'user': userdata, 'alluser': alluser, 'showuser': showuser})
