from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import json
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
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = str(request.body.decode('utf-8')).replace('\'', '\"')
        json_data = json.loads(data)
        name = json_data['name']
        surename = json_data['surename']
        city = json_data['city']
        birthday = json_data['birthday']

        if name and surename and city and birthday:
            author = Authors.objects.create(name=name, surename=surename, city=city, birthday=birthday)
            return Response(author, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


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