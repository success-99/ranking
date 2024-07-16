from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg import openapi


class JWTSchemGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self):
        security_definitions = super().get_security_definitions()
        security_definitions['Bearer'] = {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
        return security_definitions


schema_view = get_schema_view(
    openapi.Info(
        title=" REST API",
        default_version='v1',
        description="Swagger doc for REST API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="abdusalomovshaxobiddin@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    generator_class=JWTSchemGenerator
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include([
                      path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                      path('', include('category.urls')),

                      path('user/', include('users.urls')),
                      # path('delete-all-database/', include('users.remove_database.urls')),

                  ]
                  ))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'category.views.handling_404'
# handler500 = 'category.views.handling_500'