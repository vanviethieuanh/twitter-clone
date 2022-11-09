from django.contrib.auth.models import AbstractUser
from django.db import models

from django.apps import apps

import uuid


class User(AbstractUser):

    @property
    def follower_count(self):
        return apps.get_model('twitter.Follow').objects.filter(following=self).count()

    @property
    def following_count(self):
        return apps.get_model('twitter.Follow').objects.filter(follower=self).count()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
