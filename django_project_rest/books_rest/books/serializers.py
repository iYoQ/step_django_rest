from django.db.models import fields
from rest_framework import serializers
from .models import *


class AuthorsSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Authors
        fields = ['id', 'name', 'surename', 'fathername', 'city', 'birthday']


class BooksSerializer(serializers.ModelSerializer):

    class Meta():
        model = Books
        fields = ['name', 'write_date', 'description', 'pages', 'image', 'author_relative', 'publishing_relative']


class PublishingsSerializer(serializers.ModelSerializer):

    class Meta():
        model = Publishings
        fields = ['name']


class ShopSerializer(serializers.ModelSerializer):

    class Meta():
        model = Shop
        fields = ['name', 'adress', 'phone', 'assortiment']