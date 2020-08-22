from django.urls import path
from .views import AllPost, Tweet

urlpatterns = [
    path("posts/all", AllPost.as_view(), name="all_posts"),
    path("posts/tweet", Tweet.as_view(), name="tweet")
]
