from drf_yasg import openapi
from drf_yasg import views

SCHEMA_VIEW = views.get_schema_view(
    openapi.Info(
        title="Twitter APIs",
        default_version="1.0.0",
        description="API documentation"
    ),
    public=True
)
