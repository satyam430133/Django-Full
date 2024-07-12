from django.shortcuts import render,redirect

# Create your views here.
def Home(req):
    return render(req,'index.html')


def Management(req,pk):
    return render(req,'index.html')