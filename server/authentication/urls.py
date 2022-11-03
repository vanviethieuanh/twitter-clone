from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [
    path('user-info', UserInfoView.as_view()),
    path('used-email', check_used_email),
    path('register', Register.as_view()),

    # path("posts/all", AllPost.as_view(), name="all_posts"),
    # path("posts/tweet", Tweet.as_view(), name="tweet"),
    # path("posts/following", FollowingPosts.as_view(), name="following_post"),

    # path("follow/following", Following.as_view(), name="following"),
    # path("follow/follow", Follow.as_view(), name="follow"),
    # path("follow/unfollow", Unfollow.as_view(), name="unfollow"),

    # path('user/info', UserInfo.as_view(), name='user-detail'),
]
