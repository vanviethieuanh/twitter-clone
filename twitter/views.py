from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .models import Post, FollowConnect

from json import loads

from twitter.serializers import PostSerializer, FollowingSerializer, UserSerializer

class AllPost(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = JWTAuthentication().authenticate(request=request)[0]

        postsSerializer = PostSerializer(Post.objects.all(), many=True)
        user = UserSerializer(user)
        return Response({"user":user.data, "posts":postsSerializer.data})

class FollowingPosts(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = JWTAuthentication().authenticate(request=request)[0]

        following = FollowConnect.objects.filter(follower=user).values('following')
        posts = Post.objects.filter(author__in=following)

        postsSerializer = PostSerializer(posts, many=True)
        user = UserSerializer(user)
        return Response({"user":user.data, "posts":postsSerializer.data})

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

class UserInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        pk = loads(request.body)['user_id']

        user = User.objects.get(pk=pk)
        
        followings = FollowConnect.objects.filter(follower=user).count()
        followers = FollowConnect.objects.filter(following=user).count()

        posts = Post.objects.filter(author=user).count()

        userInfo = UserSerializer(user).data
        userInfo['posts'] = posts
        userInfo['followers'] = followers
        userInfo['followings'] = followings

        return Response(userInfo)