from django.urls import path, include
from users.urls import users_router
from blog.urls import blog_router, posts_router
from shop.urls import shop_router, products_router, chapters_router
from settings.urls import settings_router

# Combine all URL patterns
urlpatterns = [
    path('users/', include(users_router.urls)),
    path('blog/', include(blog_router.urls + posts_router.urls)),
    path('shop/', include(shop_router.urls + products_router.urls + chapters_router.urls)),
    path('settings/', include(settings_router.urls)),
]
