from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


# schema view description for swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Extrass 2.0 API",
      default_version='v1',
      description="Hackathon 2020",
      contact=openapi.Contact(email="raushan.kumar@itilite.com"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)

# Admin schema customization
admin.site.site_header = "Extrasss 2.0 Admin"
admin.site.site_title = "Hackathon 2020"
admin.site.index_title = "Hackathon 2020"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('offer/', include('offer.urls')),
    path('voucher/', include('voucher.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
   path('', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc',
                                      cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
