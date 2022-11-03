"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns = [
    # Swagger
    path('swagger', SCHEMA_VIEW.with_ui(
        'swagger', cache_timeout=0), name='swagger-schema'),

    path('', include('twitter.urls')),
    path('auth/', include('authentication.urls')),

    path("register", Register.as_view(), name="register"),

    path("used/email", isUsedEmail.as_view(), name="isUsedEmail"),

    path('login/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('admin/', admin.site.urls),
]
