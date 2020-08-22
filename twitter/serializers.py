from django.contrib.auth.models import User
from .models import Post, FollowConnect

from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    author_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta():
        model = Post
        fields = ['author', 'author_id' , 'post', 'post_date']

class FollowingSerializer(serializers.ModelSerializer):
    class Meta():
        model = FollowConnect
        fields = ['following']