from django.contrib import admin
from .models import Post, Category, PostMeta

class PostMetaInline(admin.TabularInline):
    model = PostMeta
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published', 'created_at')
    list_filter = ('published', 'category', 'author')
    search_fields = ('title', 'summary', 'content')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PostMetaInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'summary', 'content', 'featured_image')
        }),
        ('Category and Tags', {
            'fields': ('category', 'tags')
        }),
        ('Publication', {
            'fields': ('published', 'published_at')
        }),
        ('SEO', {
            'fields': ('_meta_title', '_meta_description', '_meta_keywords'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)} 