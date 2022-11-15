from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from twitter.models import Follow


class FollowingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Follow
        fields = ('following', 'follower', 'id')

        read_only_fields = ('id',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['following', 'follower']
            )
        ]
