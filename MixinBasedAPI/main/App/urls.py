from django.urls import path
from .views import *

urlpatterns = [
    path('stu-list/', StudentList.as_view(), name='stu-list/'),
    path('stu-info/<pk>', StudentDetails.as_view())
]
