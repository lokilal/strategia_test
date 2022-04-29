from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('openapi/', get_schema_view(
        title="Тестовое задание для Strategia",
        description="Задание: Реализовать REST API для системы комментариев блога."
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
