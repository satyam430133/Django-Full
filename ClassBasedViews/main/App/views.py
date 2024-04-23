from django.shortcuts import render
from .models import MovieModel
from .serializers import MovieSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MovieModelList(APIView):
    def get(self, request, format=None):
        MovieModels = MovieModel.objects.all()
        serializer = MovieSerializers(MovieModels, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Home(APIView):
    def get(self,request):
        movielist = MovieModel.objects.all()
        return render(request,'index.html',{'movielist':movielist})