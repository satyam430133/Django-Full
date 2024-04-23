from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = ListModel.objects.all()    