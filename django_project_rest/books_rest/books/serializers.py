from rest_framework import serializers
from .models import *


class AuthorsSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Authors()
        fields = ['id', 'name', 'surename', 'fathername', 'city', 'birthday']