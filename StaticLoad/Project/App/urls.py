from django.urls import path
from .views import *

urlpatterns = [
    path('home/',Home,name='index'),
    path('about/',About,name='about'),
    path('contect/',Contect,name='contect'),
]