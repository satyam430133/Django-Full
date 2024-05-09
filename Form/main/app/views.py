from django.shortcuts import render, HttpResponse, redirect
from .models import InfoModel
from app.forms import StudentForm

def Home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Data Saved"
            return render(request, 'index.html', {'key': msg})
    else:
        form = StudentForm()
    return render(request, 'index.html', {'form': form})

def Registration(request):
    if request.method == 'POST':
        Names = request.POST.get('Name')
        Emails = request.POST.get('Email')
        Passwords = request.POST.get('Password')
        if Names and Emails and Passwords != '':
            fill = InfoModel.objects.filter(Email=Emails)
            if fill:
                msg = "already registered"
                return redirect('index')
            else:
                msg = "Data Saved"
                okay = InfoModel.objects.create(Name=Names, Email=Emails, Password=Passwords)
            return render(request, 'index.html', {'key': msg})
        else:
            msg = "Please Fill Details"
            return render(request, 'index.html', {'key': msg})
        return redirect('index')
    else:
        return render(request, 'index.html')
