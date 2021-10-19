from django.urls import path
from .views import *


urlpatterns = [
    path('authors/', AuthorsView.as_view()),
    path('books/', BooksView.as_view()),
    path('shops/', ShopView.as_view()),
]