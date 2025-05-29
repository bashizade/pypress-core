from django.urls import path, include
from users.urls import users_router
from blog.urls import blog_router
from shop.urls import shop_router, products_router, chapters_router
from settings.urls import settings_router

urlpatterns = [
    path('users/', include(users_router)),
    path('blog/', include(blog_router)),
    path('shop/', include(shop_router)),
    path('shop/products/', include(products_router)),
    path('shop/chapters/', include(chapters_router)),
    path('settings/', include(settings_router)),
]
