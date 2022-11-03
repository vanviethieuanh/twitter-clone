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


class PostView(views.APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        """
        Return a list of posts.
        """
        follower = request.query_params.get('follower')

        if follower is not None:
            follow_users = Follow.objects.filter(
                follower=follower).values('following')
            queryset = Post.objects.filter(author__in=follow_users)

        return response.Response(queryset)

    def post(self, request, format=None):
        user = JWTAuthentication().authenticate(request=request)[0]
        return response.Response(UserSerializer(user).data)


class PostListView(generics.ListAPIView):
    """
    Function include: Retrive a list of all post
    """
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        follower = self.request.query_params.get('follower')

        if follower is not None:
            follow_users = Follow.objects.filter(
                follower=follower).values('following')
            queryset = Post.objects.filter(author__in=follow_users)

        return queryset


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


# class PostView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
