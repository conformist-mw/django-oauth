from rest_framework import permissions, viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
