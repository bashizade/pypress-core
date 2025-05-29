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
    description = models.TextField(blank=True)
    
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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = TaggableManager()
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    
    # SEO Fields
    _meta_title = models.CharField(max_length=200, blank=True)
    _meta_description = models.TextField(blank=True)
    _meta_keywords = models.CharField(max_length=200, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-published_at', '-created_at']
        
    def __str__(self):
        return self.title

class PostMeta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='meta')
    key = models.CharField(max_length=100)
    value = models.TextField()
    
    class Meta:
        verbose_name = _('post meta')
        verbose_name_plural = _('post meta')
        unique_together = ('post', 'key')
        
    def __str__(self):
        return f"{self.post.title} - {self.key}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}" 