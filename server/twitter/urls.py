from django.urls import path, include
from .views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'posts', PostView, basename='Post')


urlpatterns = [
    path('posts', PostView.as_view()),
    path('posts/following', FollowingPostView.as_view()),
    path('posts/all', AllPostView.as_view()),

    path("follow", FollowView.as_view(), name="following"),

    # path('user/info', UserInfo.as_view(), name='user-detail'),
]
