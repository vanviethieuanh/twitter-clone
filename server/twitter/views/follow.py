from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics
from rest_framework import views
from rest_framework import viewsets
from rest_framework import response
from rest_framework import permissions
from rest_framework import authentication

from rest_framework.decorators import api_view

from ..models import Follow
from django.contrib.auth.models import User

from ..serializers import FollowingSerializer
from ..serializers import UserSerializer


class FollowView(generics.RetrieveUpdateDestroyAPIView):
    """
    Follow or Unfollow a user
    """
    permission_classes = permissions.IsAuthenticatedOrReadOnly
    serializer_class = FollowingSerializer

    queryset = Follow.objects.all()
