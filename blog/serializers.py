from rest_framework import serializers
from .models import Post, Category, Tag, Comment, PostMeta

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'parent', 'created_at', 'updated_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']

class PostMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMeta
        fields = ['key', 'value']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'updated_at', 'is_approved', 'replies']
        read_only_fields = ['is_approved']

    def get_replies(self, obj):
        if obj.parent is None:  # Only get replies for parent comments
            replies = Comment.objects.filter(parent=obj, is_approved=True)
            return CommentSerializer(replies, many=True).data
        return []

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    metadata = PostMetaSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='blog:post-detail')

    class Meta:
        model = Post
        fields = [
            'id', 'uuid', 'title', 'slug', 'author', 'content', 'excerpt',
            'featured_image', 'categories', 'tags', 'status', 'created_at',
            'updated_at', 'published_at', 'views_count', 'comment_count',
            'is_featured', 'comments', 'metadata', 'url'
        ]
        read_only_fields = ['views_count', 'comment_count']

    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj, parent=None, is_approved=True)
        return CommentSerializer(comments, many=True).data

class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    categories = CategorySerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='blog:post-detail')

    class Meta:
        model = Post
        fields = [
            'id', 'uuid', 'title', 'slug', 'author', 'excerpt',
            'featured_image', 'categories', 'status', 'published_at',
            'views_count', 'comment_count', 'is_featured', 'url'
        ] 