from django.urls import path
from .views import *

urlpatterns = [
    path("posts/all", AllPost.as_view(), name="all_posts"),
    path("posts/tweet", Tweet.as_view(), name="tweet"),
    path("posts/following", FollowingPosts.as_view(), name="following_post"),

    path("follow/following", Following.as_view(), name="following"),
    path("follow/follow", Follow.as_view(), name="follow")
]
