from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'site_description', 'logo')
        }),
        ('Contact Information', {
            'fields': ('contact_mobile', 'contact_email', 'contact_address')
        }),
        ('Social Media Links', {
            'fields': ('telegram_link', 'whatsapp_link', 'instagram_link',
                      'twitter_link', 'facebook_link')
        }),
        ('SEO Settings', {
            'fields': ('_meta_title', '_meta_description', '_meta_keywords'),
            'classes': ('collapse',)
        }),
    ) 