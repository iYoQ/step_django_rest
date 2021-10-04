from rest_framework import viewsets
from .models import *
from .serializers import *


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer()