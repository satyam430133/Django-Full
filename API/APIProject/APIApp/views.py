from django.shortcuts import render,HttpResponse
from .models import *
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .serializer import *
# Create your views here.
def home(request0):
    return HttpResponse("Server is running Properly")

def stulist(request):
    stulist = StudentModel.objects.all()
    print("Query Set :",stulist)
    serializer = StudentSerializer(stulist,many=True)
    print("serializer :",serializer)
    print("Python Data :",serializer.data)
    jsonData = JSONRenderer().render(serializer.data)
    print("JSON Data :",jsonData)
    return HttpResponse(jsonData,content_type="application/json")

def stu_details(request,pk):
    studetails = StudentModel.objects.get(pk=pk)
    serializer = StudentSerializer(studetails)
    jsonData = JSONRenderer().render(serializer.data)
    return HttpResponse(jsonData,content_type='application/json')