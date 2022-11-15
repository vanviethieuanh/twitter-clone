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
from django.urls import path, re_path

from .views import *


urlpatterns = [
    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            SCHEMA_VIEW.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', SCHEMA_VIEW.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', SCHEMA_VIEW.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
    path(r'', SCHEMA_VIEW.with_ui('swagger',
                                  cache_timeout=0), name='schema-swagger-ui'),

    # Admin site
    path('admin/', admin.site.urls),

    # Auth app
    path('auth/', include('authentication.urls')),

    # Twitter
    path('', include('twitter.urls')),
]
