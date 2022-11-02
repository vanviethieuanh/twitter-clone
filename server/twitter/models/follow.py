from django.db import models
from django.contrib.auth.models import User


class Follow(models.Model):

    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')

    def __str__(self):
        return "{follower} is following {following}".format(follower=self.follower, following=self.following)

    def get_absolute_url(self):
        return reverse("follow_detail", kwargs={"pk": self.pk})
