from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from .models import Post, Category, PostMeta, Comment
from .serializers import (
    PostSerializer, CategorySerializer, PostMetaSerializer,
    CommentSerializer
)

class PostFilter(FilterSet):
    tags = CharFilter(method='filter_tags')
    
    def filter_tags(self, queryset, name, value):
        return queryset.filter(tags__name__in=[value])
    
    class Meta:
        model = Post
        fields = {
            'category': ['exact'],
            'author': ['exact'],
            'is_published': ['exact'],
            'created_at': ['gte', 'lte'],
            'updated_at': ['gte', 'lte'],
            'published_at': ['gte', 'lte'],
        }

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'author', 'tags']
    search_fields = ['title', 'content', 'summary']
    ordering_fields = ['published_at', 'created_at', 'updated_at']
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name']
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['post', 'user', 'is_approved']
    ordering_fields = ['created_at', 'updated_at']
    
    def get_queryset(self):
        return Comment.objects.filter(is_approved=True)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 