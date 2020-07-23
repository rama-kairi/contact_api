from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Documentation

schema_view = get_schema_view(
    openapi.Info(
        title="Contact List API",
        default_version='v1',
        description="An API for the Contact List",
        terms_of_service="https://digitalrama.co.in/policies/terms/",
        contact=openapi.Contact(email="contact@digitalrama.co.in"),
        license=openapi.License(name="Public"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/contacts/', include('contacts.urls')),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc',
                                      cache_timeout=0), name='schema-redoc')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
