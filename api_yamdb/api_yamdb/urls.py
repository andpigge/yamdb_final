from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from .yasg import urlpatterns as swagger_urls

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    )
]

urlpatterns += swagger_urls
