from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name = 'home'),
    path('about/', about, name='about'),
    path('userform/',userForm,name='userform' ),
    path('calculator/',calculator,name='calculator'),
    path('evenOdd/',evenOdd,name='evenOdd'),
    path('marksheet/',marksheet,name='marksheet'),
    path('servicedata/',servicedata,name='servicedata'),    
    path('servicedata/newsdetails/<slug>',newsdetails,name='newsdetails')
    # path('submitform',submitform,name='submitform'),
    # path('home/',home, name = 'home'),
    # path('urlll', urlll, name = 'urlll'),
    # path('urlll/<courceId>', courceDetails),
    # path('Homepage/', Homepage, name = 'Homepage'),
]
