from rest_framework import routers
from books.viewsets import *
from user.viewsets import *

router = routers.DefaultRouter()
router.register('authors', AuthorsViewSet)
router.register('books', BooksViewSet)
router.register('publishings', PublishingsViewSet)
router.register('shop', ShopViewSet)
router.register('users', UserViewSet)