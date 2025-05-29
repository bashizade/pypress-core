from rest_framework import serializers
from .models import Post, Category, PostMeta
from users.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'parent')

class PostMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMeta
        fields = ('key', 'value')

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        source='category'
    )
    meta_fields = PostMetaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'summary', 'content', 'featured_image',
                 'category', 'category_id', 'tags', 'author', 'created_at',
                 'updated_at', 'published', 'published_at', 'meta_fields',
                 '_meta_title', '_meta_description', '_meta_keywords')
        read_only_fields = ('id', 'created_at', 'updated_at', 'published_at') 