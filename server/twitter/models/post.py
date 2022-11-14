from django.db import models

from authentication.models import User


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author')
    post = models.CharField('Post', max_length=280)
    post_date = models.DateTimeField("Post date", auto_now_add=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

        ordering = ['-post_date']

    @property
    def author_email(self):
        return self.author.email

    @property
    def author_username(self):
        return self.author.username

    def __str__(self):
        return self.post
