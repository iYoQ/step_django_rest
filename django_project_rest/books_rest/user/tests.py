from django.test import TestCase
from django.urls import reverse
from user.views import UserAction
from .models import *
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate


class UserTestCase(APITestCase):
    def setUp(self):
        self.user_data = User.objects.create(email='admin@admin.com', password='admin')

    def test_me(self):
        factory = APIRequestFactory()

        user = User.objects.get(email='admin@admin.com')
        view = UserAction.as_view()

        request = factory.get(reverse('me'), content_type='application/json')
        force_authenticate(request, user=user)
        response = view(request)
        
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
