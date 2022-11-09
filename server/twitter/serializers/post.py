from rest_framework import serializers

from twitter.models import Post
from authentication.models import User


class PostSerializer(serializers.ModelSerializer):

    class Meta():
        model = Post
        read_only_fields = ('post_date', 'author', 'id',
                            'author_email', 'author_username')
        fields = ('post',) + read_only_fields

    def create(self, author: User):
        post = Post(
            author=author,
            post=self.validated_data['post']
        )

        post.save()
        return post
