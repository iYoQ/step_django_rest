from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class AuthorsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('city', )


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class PublishingsViewSet(viewsets.ModelViewSet):
    queryset = Publishings.objects.all()
    serializer_class = PublishingsSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer