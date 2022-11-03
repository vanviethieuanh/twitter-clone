from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics
from rest_framework import response
from rest_framework import permissions
from rest_framework import views

from twitter.models import Post
from twitter.models import Follow

from twitter.serializers import PostSerializer


class PostView(views.APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        """
        Return a list of posts.
        """
        is_following_posts = request.query_params.get('following')
        follower = request.user

        if is_following_posts:
            follow_users = Follow.objects.filter(
                follower=follower
            ).values('following')
            queryset = Post.objects.filter(author__in=follow_users)

        return response.Response(queryset)

    def post(self, request, format=None):
        author = request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = serializer.create(author)

        return response.Response(self.serializer_class(post).data)

    def delete(self, request, format=None):
        pass
