from rest_framework import serializers
from .models import User
from .services import send_email


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(**validated_data)
        password = validated_data.get('password', None)
        user.set_password(password)
        user.save()
        send_email.delay()
        return user


    class Meta():
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'patronymic', 'is_active', 'is_superuser', 'post_agreement', 'tin', 'bank_account', 'phone', 'address']
    