from django.contrib.auth.models import User
from .models import Post

from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    class Meta():
        model = Post
        fields = ['author', 'post', 'post_date']