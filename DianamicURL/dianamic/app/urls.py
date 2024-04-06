from django.urls import path
from .views import *

urlpatterns = [
    path('home/<path:PK>', home, name='name'),
    path("combination/<int:ab>/<str:string>/<slug:slugdata>",combination,name='combination')
]