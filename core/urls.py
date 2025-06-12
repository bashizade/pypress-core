from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    
    # API endpoints
    path('api/', include('api.urls')),
    
    # Authentication endpoints
    path('accounts/', include('allauth.urls')),

    path("i18n/", include("django.conf.urls.i18n")),
]+ i18n_patterns(
        path("admin/", admin.site.urls),
    )

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 