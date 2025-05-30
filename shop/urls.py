from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

# Main router for shop resources
shop_router = DefaultRouter()
shop_router.register(r'categories', views.CategoryViewSet, basename='category')
shop_router.register(r'products', views.ProductViewSet, basename='product')
shop_router.register(r'attributes', views.ProductAttributeViewSet, basename='attribute')
shop_router.register(r'shipping-methods', views.ShippingMethodViewSet, basename='shipping-method')
shop_router.register(r'shipping-zones', views.ShippingZoneViewSet, basename='shipping-zone')
shop_router.register(r'discount-codes', views.DiscountCodeViewSet, basename='discount-code')

# Nested routers for product-related resources
products_router = routers.NestedDefaultRouter(shop_router, r'products', lookup='product')
products_router.register(r'variants', views.ProductVariantViewSet, basename='product-variants')
products_router.register(r'chapters', views.ChapterViewSet, basename='product-chapters')
products_router.register(r'reviews', views.ReviewViewSet, basename='product-reviews')

# Nested router for chapters
chapters_router = routers.NestedDefaultRouter(products_router, r'chapters', lookup='chapter')
chapters_router.register(r'lessons', views.LessonViewSet, basename='chapter-lessons')

# User-specific resources
class UserResourceRouter(DefaultRouter):
    def get_urls(self):
        urls = super().get_urls()
        return [
            path('users/<int:user_pk>/orders/', views.OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-orders'),
            path('users/<int:user_pk>/orders/<int:pk>/', views.OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-orders-detail'),
            path('users/<int:user_pk>/cart/', views.CartViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='user-cart'),
            path('users/<int:user_pk>/cart/items/', views.CartItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-cart-items'),
            path('users/<int:user_pk>/cart/items/<int:pk>/', views.CartItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-cart-items-detail'),
        ] + urls

user_router = UserResourceRouter()

# Combine all URL patterns
urlpatterns = shop_router.urls + products_router.urls + chapters_router.urls + user_router.urls + [
    path('validate-discount-code/', views.ValidateDiscountCodeView.as_view(), name='validate-discount-code'),
]