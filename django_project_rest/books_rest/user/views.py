from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import UserSerializer
from .models import User


class UserAction(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_data = UserSerializer(User.objects.filter(pk=self.request.user.pk).first())
        return Response(data=user_data.data, status=status.HTTP_200_OK)