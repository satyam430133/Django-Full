from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='index'),
    path('register/',Registration,name='register'),
    path('login/',Login,name='login')
]
