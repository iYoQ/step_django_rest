from rest_framework import serializers, status
from rest_framework.response import Response
from .models import *


class AuthorsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # return Authors.objects.create_author(name=validated_data['name'], surename=validated_data['surename'], fathername=validated_data['fathername'], city=validated_data['city'], birthday=validated_data['birthday'])

        author = Authors(**validated_data)
        author.save()
        return author


    class Meta():
        model = Authors
        fields = ['name', 'surename', 'birthday']


class BooksSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Books.objects.create_book(name=validated_data['name'], write_date=validated_data['write_date'], description=validated_data['description'], pages=validated_data['pages'], image=validated_data['image'], author_relative=validated_data['author_relative'], publishing_relative=validated_data['publishing_relative'])

    author_relative = AuthorsSerializer(read_only=True)

    class Meta():
        model = Books
        fields = ['name', 'write_date', 'description', 'pages', 'image', 'author_relative', 'publishing_relative']


class PublishingsSerializer(serializers.ModelSerializer):

    class Meta():
        model = Publishings
        fields = ['name']


class ShopSerializer(serializers.ModelSerializer):

    assortiment = BooksSerializer(read_only=True, many=True)

    class Meta():
        model = Shop
        fields = ['name', 'adress', 'phone', 'assortiment']