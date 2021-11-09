from django.test import TestCase
from .models import *
from rest_framework import status
from django.test import Client
from rest_framework.test import APIClient, APITestCase


class RegistrationTestCase(APITestCase):
    def test_user_authorization(self):
        data = {
            'email': 'admin@admin.com',
            'password': 'admin',
        }
        c = APIClient()
        # c.login(email='admin@admin.com', password='admin')
        response = c.post('/user/token/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
