from rest_framework import serializers
from .models import Post, Category, PostMeta, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent', 'description']

class PostMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMeta
        fields = ['key', 'value']

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = [
            'id', 'user', 'content', 'is_approved',
            'created_at', 'updated_at', 'replies'
        ]
        read_only_fields = ['user', 'is_approved', 'created_at', 'updated_at']
    
    def get_replies(self, obj):
        if obj.parent is None:  # Only get replies for top-level comments
            replies = Comment.objects.filter(parent=obj, is_approved=True)
            return CommentSerializer(replies, many=True).data
        return []

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        source='category'
    )
    meta = PostMetaSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'summary', 'content',
            'featured_image', 'author', 'category', 'category_id',
            'tags', 'is_published', 'published_at', 'meta',
            'comments', 'created_at', 'updated_at'
        ]
        read_only_fields = ['slug', 'author', 'created_at', 'updated_at'] 