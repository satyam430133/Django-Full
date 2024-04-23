from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import *
from .serializers import *

# Create your views here.

class StudentList(APIView):
    def get(self,request,format=True):
        stulist = StudentModel.objects.all()
        serializers = StudentSerializer(stulist,many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetails(APIView):
    def get(self,request,pk,format=True):
        stulist = StudentModel.objects.get(pk=pk)
        serializers = StudentSerializer(stulist)
        return Response(serializers.data)
    def put(self,request,pk,format=True):
        stulist = StudentModel.objects.get(pk=pk)
        serializers = StudentSerializer(stulist,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else: return Response(serializers.errors)
    def delete(self,request,pk,format=True):
        stulist = StudentModel.objects.get(pk=pk)
        stulist.delete()
        return Response({'error':"Data Deleted Successfully"},status=status.HTTP_404_NOT_FOUND)


# from .models import *
# from .serializers import *
# from rest_framework import generics

# class StudentList(generics.ListCreateAPIView):
#     queryset = StudentModel.objects.all()
#     serializer_class = StudentSerializer

# class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StudentModel.objects.all()
#     serializer_class = StudentSerializer