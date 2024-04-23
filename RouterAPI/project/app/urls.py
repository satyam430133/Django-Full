from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework import viewsets
from .views import *

router = routers.DefaultRouter()
router.register(r'list',ListViewSet,basename='list')

urlpatterns = [
    path('',include(router.urls)),
]