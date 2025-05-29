from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'attributes', views.ProductAttributeViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'variants', views.ProductVariantViewSet)
router.register(r'shipping-methods', views.ShippingMethodViewSet)
router.register(r'shipping-zones', views.ShippingZoneViewSet)
router.register(r'orders', views.OrderViewSet, basename='order')
router.register(r'cart', views.CartViewSet, basename='cart')
router.register(r'cart-items', views.CartItemViewSet, basename='cart-item')
router.register(r'reviews', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 