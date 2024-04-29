from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly

class MovieViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]
	queryset = MovieModel.objects.all()
	serializer_class = MovieSerializer

class StudentViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser]
	queryset = StudentModel.objects.all()
	serializer_class = StudentSerializer

class ArtStudentViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAdminUser]
	queryset = ArtStudentModel.objects.all()
	serializer_class = StudentSerializer

class BioStudentViewSet(viewsets.ModelViewSet):
	permission_classes = [AllowAny]
	queryset = BioStudentModel.objects.all()
	serializer_class = StudentSerializer

class MathStudentViewSet(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = MathStudentModel.objects.all()
	serializer_class = StudentSerializer