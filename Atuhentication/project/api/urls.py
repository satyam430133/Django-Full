from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
# import routers
from rest_framework import routers
# import everything from views
from .views import *
  
# define the router
router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet)
router.register(r'student', StudentViewSet)
router.register(r'artstudent', ArtStudentViewSet)
router.register(r'biostudent', BioStudentViewSet)
router.register(r'mathstudent', MathStudentViewSet)
  
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token)
]