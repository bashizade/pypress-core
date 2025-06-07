from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Post, Category, PostMeta, Comment

class PostMetaInline(admin.TabularInline):
    model = PostMeta
    extra = 1

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_published', 'published_at', 'created_at']
    list_filter = ['is_published', 'category', 'author', 'created_at']
    search_fields = ['title', 'content', 'summary']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    readonly_fields = ['created_at', 'updated_at']
    inlines = [PostMetaInline]
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'summary', 'content', 'featured_image')
        }),
        ('Relations', {
            'fields': ('author', 'category', 'tags')
        }),
        ('Publication', {
            'fields': ('is_published', 'published_at')
        }),
        ('SEO', {
            'fields': ('_meta_title', '_meta_description', '_meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'parent', 'description']
    list_filter = ['parent']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PostMeta)
class PostMetaAdmin(ModelAdmin):
    list_display = ['post', 'key', 'value']
    list_filter = ['post']
    search_fields = ['post__title', 'key', 'value']

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ['post', 'user', 'content', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['post__title', 'user__username', 'content']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        (None, {
            'fields': ('post', 'user', 'parent', 'content')
        }),
        ('Status', {
            'fields': ('is_approved',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    ) 