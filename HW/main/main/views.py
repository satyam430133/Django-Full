from django.shortcuts import render,HttpResponse

def Home(request):
    return render(request, 'index.html')

def Menu(request):
    return render(request, 'menu.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')