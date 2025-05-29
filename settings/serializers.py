from rest_framework import serializers
from .models import SiteSettings

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = ('id', 'site_name', 'site_description', 'logo',
                 'contact_mobile', 'contact_email', 'contact_address',
                 'telegram_link', 'whatsapp_link', 'instagram_link',
                 'twitter_link', 'facebook_link',
                 '_meta_title', '_meta_description', '_meta_keywords')
        read_only_fields = ('id',) 