from rest_framework import serializers
from .models import User
from .services import send_email


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User(**validated_data)
        password = validated_data.get('password', None)
        if password.length() < 8:
            raise ValueError('password length too short')
        user.set_password(password)
        # send_email.delay()
        user.save()
        return user


    class Meta():
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'patronymic', 'is_active', 'is_superuser', 'post_agreement', 'tin', 'bank_account', 'phone', 'address']
    