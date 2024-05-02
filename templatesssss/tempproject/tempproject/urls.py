"""
URL configuration for tempproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from tempApp1.views import app1home1
# from tempApp2.views import app2home1

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('app1home1',app1home1),
    # path('app2home1',app2home1),
    path('app1/',include('tempApp1.urls')),
    path('app2/',include('tempApp2.urls')),
]