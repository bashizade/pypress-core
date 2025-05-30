from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

settings_router = DefaultRouter()
settings_router.register(r'settings', views.SiteSettingsViewSet, basename='settings')

urlpatterns = settings_router.urls