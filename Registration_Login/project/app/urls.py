from django.urls import path
from .views import home, Registration, Login, AddQuery, SubmitQuery, Show, EditQuery, UpdateData, DeleteQuery

urlpatterns = [
    path('', home, name='index'),
    path('register/', Registration, name='register'),
    path('login/', Login, name='login'),
    path('query/<pk>/', AddQuery, name='query'),
    path('submitquery/<pk>/', SubmitQuery, name='submitquery'),
    path('show/<pk>/', Show, name='show'),
    path('editquery/<pk>/', EditQuery, name='editquery'),
    path('update/<pk>/', UpdateData, name='update'),
    path('delete/<pk>/<ml>/', DeleteQuery, name='delete'),
]
