from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIRequestFactory
from .models import *


class BooksTestCase(TestCase):
    def setUp(self) -> None:
        image = SimpleUploadedFile('la_divina_commedia.jpg', content=b'', content_type='image')

        self.author = Authors.objects.create(name='Dante', surename='Alighieri', fathername='', city='Florence', birthday='1265-01-01')
        self.books = Books.objects.create(name='Divine Comedy', write_date='1320-01-01', description='Divine Comedy desc', pages=300, image=image, author_relative=self.author, publishing_relative=None)

    # def setUp(self) -> None:
    #     image = SimpleUploadedFile('la_divina_commedia.jpg', content=b'', content_type='image')

        # self.author = {'name': 'Dante', 'surename': 'Alighieri', 'fathername': '', 'city': 'Florence', 'birthday': '1265-01-01'}
        # self.books = {'name': 'Divine Comedy', 'write_date': '1320-01-01', 'description': 'Divine Comedy desc', 'pages': 300, 'image': image, 'author_relative': '', 'publishing_relative': None}

    # def test_save_book(self):
    #     Authors.objects.create(name=self.author['name'], surename=self.author['surename'], fathername=self.author['fathername'], city=self.author['city'], birthday=self.author['birthday'])
    #     Books.objects.create(name=self.books['name'], write_date=self.books['write_date'], description=self.books['description'], pages=self.books['pages'], image=self.books['image'], author_relative=Authors.objects.latest('id'), publishing_relative=self.books['publishing_relative'])

    #     print('Save book case complete')
    
    # def test_post_book(self):
    #     factory = APIRequestFactory()
    #     request = 