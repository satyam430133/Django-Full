from django.urls import path
from .views import *

urlpatterns = [
    path('itemlist',Item_List,name='itemlist'),
    path('item/<pk>',Item,name='item')
]
