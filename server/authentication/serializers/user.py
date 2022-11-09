from authentication.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        read_only_fields = ('follower_count', 'following_count', 'post_count')
        fields = ('id',
                  'username', 'password', 'email',
                  'first_name', 'last_name',) + read_only_fields

        extra_kwargs = {'password': {'write_only': True}}

    def create(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        user.set_password(self.validated_data['password'])
        user.save()

        return user
