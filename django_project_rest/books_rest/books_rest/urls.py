"""books_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .router import router
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from user.views import UserAction


schema_view = get_swagger_view(title='Books API')

urlpatterns = [
    url('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('user/', include('user.urls')),
    path('api-auth/', include(router.urls)),
    path('me/', UserAction.as_view(), name='me')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)