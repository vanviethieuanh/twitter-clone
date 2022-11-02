from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics
from rest_framework import response
from rest_framework import permissions
from rest_framework import views
from rest_framework import viewsets

from ..models import Post
from ..models import Follow

from ..serializers import PostSerializer
from ..serializers import UserSerializer


class PostListView(generics.ListAPIView):
    """
    Function include: Retrive a list of all post
    """
    permission_classes = permissions.IsAuthenticatedOrReadOnly
    serializer_class = PostSerializer

    queryset = Post.objects.all()


class FollowingPostListView(generics.ListAPIView):
    """
    Retrive a list of following post
    """
    permission_classes = permissions.IsAuthenticated
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        user = JWTAuthentication().authenticate(request=request)[0]

        follow_users = Follow.objects.filter(
            follow_user=user).values('following')
        posts = Post.objects.filter(author__in=follow_users)

        postsSerializer = PostSerializer(posts, many=True)
        user = UserSerializer(user)

        return response.Response({
            "user": user.data,
            "posts": postsSerializer.data
        })


class PostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
