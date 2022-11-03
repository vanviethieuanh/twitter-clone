from django.urls import path

from authentication.views import UserInfoView
from authentication.views import UserView
from authentication.views import check_used_email

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user-info', UserInfoView.as_view()),
    path('used-email', check_used_email),

    path('register', UserView.as_view()),

    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
