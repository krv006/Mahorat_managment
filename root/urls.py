from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.i18n import set_language
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from root import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Mahorat Management",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('set_language/', set_language, name='set_language'),
    # other non-translated URLs
]

urlpatterns += i18n_patterns(
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
