from django.urls import include, path

# import routers
from rest_framework import routers 
# import everything from views
from .views import *
  
# define the router
router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet)
router.register(r'student', StudentViewSet)
  
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # this line is used for only login & logout feature in DRF window
]