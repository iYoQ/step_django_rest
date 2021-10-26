from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
from .services import send_email


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer