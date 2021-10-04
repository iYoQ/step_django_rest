from rest_framework import routers
from books.viewsets import *

router = routers.DefaultRouter()
router.register(r'authors', AuthorsViewSet)