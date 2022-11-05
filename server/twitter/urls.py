from django.urls import path
from .views import *

urlpatterns = [
    path('posts', PostView.as_view()),
    path('posts/following', FollowingPostView.as_view()),
    path('posts/all', AllPostView.as_view()),

    path("follow", FollowView.as_view(), name="following"),
]
