from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

# Main router for blog resources
blog_router = DefaultRouter()
blog_router.register(r'categories', views.CategoryViewSet, basename='blog-category')
blog_router.register(r'posts', views.PostViewSet, basename='blog-post')

# Nested router for post-related resources
posts_router = routers.NestedDefaultRouter(blog_router, r'posts', lookup='post')
posts_router.register(r'comments', views.CommentViewSet, basename='post-comment')

urlpatterns = [
    # Main blog endpoints
    path('', include(blog_router.urls)),
    
    # Post-related endpoints
    path('posts/', include(posts_router.urls)),
]
