from rest_framework import generics
from rest_framework import response
from rest_framework import permissions
from rest_framework import views
from rest_framework import pagination
from rest_framework import exceptions

from twitter.models import Post
from twitter.models import Follow

from twitter.serializers import PostSerializer

from drf_yasg.utils import swagger_auto_schema

from common.helpers.doc import IdQueryParameter


class PostPagination(pagination.PageNumberPagination):
    max_page_size = 100


class PostView(views.APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="Create a new post."
    )
    def post(self, request, format=None):
        author = request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.create(author)

        return response.Response(self.serializer_class(post).data)

    @swagger_auto_schema(
        operation_summary="Delete a post by id.",
        manual_parameters=[
            IdQueryParameter(description='Post id to delete', required=True)
        ]
    )
    def delete(self, request, format=None):
        author = request.user

        post_id = request.query_params.get('id')
        post = Post.objects.get(pk=post_id)

        if not post:
            raise exceptions.NotFound()

        if author is not post.author:
            raise exceptions.PermissionDenied(
                detail=f'Post own by {post.author}')

        post.delete()
        return response.Response(self.serializer_class(post))


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
