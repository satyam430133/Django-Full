from django.urls import path
from .views import *
from .serializer import *
urlpatterns = [
    path('',home,name='home'),
    path('stulist',stulist,name='stulist'),
    path('stu_details/<int:pk>',stu_details,name='stu_details')
]
