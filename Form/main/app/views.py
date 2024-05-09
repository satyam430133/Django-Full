from django.shortcuts import render,HttpResponse
from .models import InfoModel
from app.forms import StudentForm
# Create your views here.

def Home(request):
    context = {}
    context['form'] = StudentForm
    return render(request, 'index.html',context)

def Registration(request):
   try:
        if request.method == 'POST':
            Names = request.POST.get('Name')
            Emails = request.POST.get('Email')
            Passwords = request.POST.get('Password')
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