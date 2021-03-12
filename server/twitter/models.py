from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    post = models.CharField('Post', max_length=280)
    post_date = models.DateTimeField("Post date", auto_now_add=True)

    class Meta:
        verbose_name = ("post")
        verbose_name_plural = ("posts")

        ordering = ['-post_date']

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

class FollowConnect(models.Model):

    following   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    def __str__(self):
        return "{follower} is following {following}".format(follower=self.follower,following=self.following)

    def get_absolute_url(self):
        return reverse("follow_detail", kwargs={"pk": self.pk})

