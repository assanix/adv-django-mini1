from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

api_info = openapi.Info(
    title="Sales & Trading API",
    default_version="v1",
    description="Documentation for the Sales and Trading API",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("oauth/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/products/", include("products.urls")),
    path("api/trading/", include("trading.urls")),
    path("api/sales/", include("sales.urls")),
    path("api/analytics/", include("analytics.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc-ui"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
