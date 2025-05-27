from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category, Tag, Comment, PostMeta

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at', 'updated_at')
    list_filter = ('parent',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class PostMetaInline(admin.TabularInline):
    model = PostMeta
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_at', 'views_count', 'comment_count', 'is_featured')
    list_filter = ('status', 'created_at', 'published_at', 'is_featured', 'categories', 'tags')
    search_fields = ('title', 'content', 'excerpt')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_at'
    filter_horizontal = ('categories', 'tags')
    inlines = [PostMetaInline]
    readonly_fields = ('views_count', 'comment_count', 'created_at', 'updated_at')
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content', 'excerpt', 'featured_image')
        }),
        ('Relations', {
            'fields': ('author', 'categories', 'tags')
        }),
        ('Status', {
            'fields': ('status', 'published_at', 'is_featured')
        }),
        ('Statistics', {
            'fields': ('views_count', 'comment_count', 'created_at', 'updated_at')
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('author')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'content_preview', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('author__username', 'content', 'post__title')
    raw_id_fields = ('post', 'author', 'parent')
    date_hierarchy = 'created_at'
    actions = ['approve_comments', 'disapprove_comments']

    def content_preview(self, obj):
        return format_html('<span title="{}">{}</span>', obj.content, obj.content[:50] + '...' if len(obj.content) > 50 else obj.content)
    content_preview.short_description = 'Content'

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Approve selected comments"

    def disapprove_comments(self, request, queryset):
        queryset.update(is_approved=False)
    disapprove_comments.short_description = "Disapprove selected comments"
