from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 12


class AuthorsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        authors = Authors.objects.all()
        serializer = AuthorsSerializer(authors, many=True)
        return Response(serializer.data)


class BooksView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = StandardResultsSetPagination
    
    # def get(self, request):
    #     books = Books.objects.all()
    #     serializer = BooksSerializer(books, many=True)
    #     return Response(serializer.data)


class ShopView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer