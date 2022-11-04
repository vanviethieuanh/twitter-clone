from rest_framework import serializers
from ..models import Follow


class FollowingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Follow
        fields = ('following', 'follower', 'id')
        read_only_fields = ('id')
