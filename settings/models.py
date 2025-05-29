from django.db import models
from django.utils.translation import gettext_lazy as _
from meta.models import ModelMeta

class SiteSettings(ModelMeta, models.Model):
    site_name = models.CharField(max_length=100)
    site_description = models.TextField()
    logo = models.ImageField(upload_to='site/')
    
    # Contact Information
    contact_mobile = models.CharField(max_length=11, blank=True)
    contact_email = models.EmailField(blank=True)
    contact_address = models.TextField(blank=True)
    
    # Social Media Links
    telegram_link = models.URLField(blank=True)
    whatsapp_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    
    # SEO Fields
    _meta_title = models.CharField(max_length=200, blank=True)
    _meta_description = models.TextField(blank=True)
    _meta_keywords = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = _('site setting')
        verbose_name_plural = _('site settings')
        
    def __str__(self):
        return self.site_name
        
    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            raise ValidationError('There can be only one SiteSettings instance')
        return super().save(*args, **kwargs) 