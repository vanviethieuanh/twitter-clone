import imp
from msilib.schema import SelfReg
from statistics import mode
from rest_framework import serializers

from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    author_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta():
        model = Post
        fields = ['author', 'author_id', 'post', 'post_date']
