from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .models import Post, FollowConnect

from json import loads

from twitter.serializers import PostSerializer, FollowingSerializer

class AllPost(APIView):
    def get(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)

class FollowingPosts(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = JWTAuthentication().authenticate(request=request)[0]

        following = FollowConnect.objects.filter(follower=user).values('following')

        posts = Post.objects.filter(author__in=following)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class Tweet(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        user = JWTAuthentication().authenticate(request=request)[0]
        
        post = Post()
        post.author = user
        post.post = loads(request.body)['post']
        post.save()

        return Response(PostSerializer(post).data)

class Follow(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        user = JWTAuthentication().authenticate(request=request)[0]
        
        if FollowConnect.objects.filter(follower=user, following=User.objects.get(pk=loads(request.body)['follow_id'])).count() >= 1:
            return Response({"message":"Follwed"})

        follow = Follow()
        follow.follower = user
        follow.following = User.objects.get(pk=loads(request.body)['follow_id'])
        follow.save()        

        return Response({"message":"Follwed"})

class Following(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = JWTAuthentication().authenticate(request=request)[0]
        followings = FollowConnect.objects.filter(follower=user)

        serializer = FollowingSerializer((followings), many=True)

        return Response(serializer.data)