from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/settings/', include('settings.urls')),
    path('accounts/', include('allauth.urls')),
    path('api/shop/', include('shop.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 