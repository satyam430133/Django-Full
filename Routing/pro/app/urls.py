from django.urls import path
from .views import *

urlpatterns = [
    path('',Home,name='index'),
    path('management/<pk>',Management,name='management'),
]