from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .models import Post

from json import loads

from twitter.serializers import PostSerializer

class AllPost(APIView):
    def get(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
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
        pass
    pass

# @api_view(['POST'])
# def Tweet(request):
#     header = JWTAuthentication().get_header(request)
#     if header is None:
#         return None

#     raw_token = JWTAuthentication().get_raw_token(header)
#     if raw_token is None:
#         return None

#     validated_token = JWTAuthentication().get_validated_token(raw_token)
#     print(validated_token)

#     return Response({})