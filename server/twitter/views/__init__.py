from .follow import FollowingSerializer, FollowView
from .post import PostListView, PostView, FollowingPostListView

from rest_framework import permissions
from rest_framework import authentication
from rest_framework import views


class BaseAuthenticatedView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class BaseAuthenticatedOrReadOnlyView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
