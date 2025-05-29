from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from meta.models import ModelMeta

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        
    def __str__(self):
        return self.name

class Post(ModelMeta, models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField()
    content = RichTextField()
    featured_image = models.ImageField(upload_to='blog/featured_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    
    # Meta fields for SEO
    _meta_title = models.CharField(max_length=200, blank=True)
    _meta_description = models.TextField(blank=True)
    _meta_keywords = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-published_at', '-created_at']
        
    def __str__(self):
        return self.title

class PostMeta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='meta_fields')
    key = models.CharField(max_length=100)
    value = models.TextField()
    
    class Meta:
        verbose_name = _('post meta')
        verbose_name_plural = _('post metas')
        unique_together = ('post', 'key')
        
    def __str__(self):
        return f"{self.post.title} - {self.key}" 