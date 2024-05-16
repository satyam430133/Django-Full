from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='index'),
    path('register/',Registration,name='register'),
    path('login/',Login,name='login'),
    path('query/<pk>',AddQuery,name='query'),
    path('submitquery/<pk>',SubmitQuery,name='submitquery'),
    path('show/<pk>',Show,name='show'),
]
