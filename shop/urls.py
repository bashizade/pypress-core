from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'attributes', views.ProductAttributeViewSet)
router.register(r'orders', views.OrderViewSet, basename='order')
router.register(r'progress', views.UserProgressViewSet, basename='progress')

# Nested routers for course content
products_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
products_router.register(r'chapters', views.ChapterViewSet, basename='product-chapters')

chapters_router = routers.NestedDefaultRouter(products_router, r'chapters', lookup='chapter')
chapters_router.register(r'lessons', views.LessonViewSet, basename='chapter-lessons')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),
    path('', include(chapters_router.urls)),
] 