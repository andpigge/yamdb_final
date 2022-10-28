from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

params = dict(
    title="API_YAMDB",
    default_version='v1',
    description="API",
    contact=openapi.Contact(email="rustamaaa@bk.ru"),
    license=openapi.License(name="MSI License"),
)

URL_SWAGGER_REGEX = r'swagger(?P\.json|\.yaml)'

""" Настройки отображения swagger. """
schema_view = get_schema_view(
    openapi.Info(**params),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        URL_SWAGGER_REGEX,
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/progect/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]
