from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from django.urls import reverse
from .views import AuthorsView
from user.views import UserAction
from user.models import User
from rest_framework import status
from .models import *


class BooksTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='admin@admin.com', password='admin')
    # def setUp(self) -> None:
    #     image = SimpleUploadedFile('la_divina_commedia.jpg', content=b'', content_type='image')

        # self.author = {'name': 'Dante', 'surename': 'Alighieri', 'fathername': '', 'city': 'Florence', 'birthday': '1265-01-01'}
        # self.books = {'name': 'Divine Comedy', 'write_date': '1320-01-01', 'description': 'Divine Comedy desc', 'pages': 300, 'image': image, 'author_relative': '', 'publishing_relative': None}

    # def test_save_book(self):
    #     Authors.objects.create(name=self.author['name'], surename=self.author['surename'], fathername=self.author['fathername'], city=self.author['city'], birthday=self.author['birthday'])
    #     Books.objects.create(name=self.books['name'], write_date=self.books['write_date'], description=self.books['description'], pages=self.books['pages'], image=self.books['image'], author_relative=Authors.objects.latest('id'), publishing_relative=self.books['publishing_relative'])

    #     print('Save book case complete')
    
    def test_post_book(self):
        factory = APIRequestFactory()

        user = User.objects.get(email='admin@admin.com')
        view = AuthorsView.as_view()
        author_json = {
            "name": "Dante", 
            "surename": "Alighieri", 
            "fathername": "", 
            "city": "Florence", 
            "birthday": "1265-01-01"
        }

        request = factory.post(reverse('authors'), data=author_json, content_type='application/json')
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)