from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics
from rest_framework import response
from rest_framework import permissions
from rest_framework import views
from rest_framework import pagination

from twitter.models import Post
from twitter.models import Follow

from twitter.serializers import PostSerializer

from drf_yasg.utils import swagger_auto_schema


class PostPagination(pagination.PageNumberPagination):
    max_page_size = 100


class PostView(views.APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        author = request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.create(author)

        return response.Response(self.serializer_class(post).data)

    def delete(self, request, format=None):
        author = request.user

        post_id = request.query_params.get('id')

        pass


class AllPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination


class FollowingPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = PostPagination

    def get_queryset(self):
        follower = self.request.user

        follow_users = Follow.objects.filter(
            follower=follower).values('following')
        queryset = Post.objects.filter(author__in=follow_users)

        return queryset
