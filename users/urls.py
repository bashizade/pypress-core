from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

# Main router for user resources
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'roles', views.RoleViewSet, basename='role')

# Nested router for user-related resources
users_router = routers.NestedDefaultRouter(router, r'users', lookup='user')
users_router.register(r'profile', views.UserProfileViewSet, basename='user-profile')

urlpatterns = [
    # Main user endpoints
    path('', include(router.urls)),
    
    # User-related endpoints
    path('users/', include(users_router.urls)),
]