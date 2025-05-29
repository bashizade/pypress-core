from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from .models import Post, Category, PostMeta
from .serializers import PostSerializer, CategorySerializer, PostMetaSerializer

class PostFilter(FilterSet):
    tags = CharFilter(method='filter_tags')
    
    def filter_tags(self, queryset, name, value):
        return queryset.filter(tags__name__in=[value])
    
    class Meta:
        model = Post
        fields = {
            'category': ['exact'],
            'author': ['exact'],
            'published': ['exact'],
            'created_at': ['gte', 'lte'],
            'updated_at': ['gte', 'lte'],
            'published_at': ['gte', 'lte'],
        }

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['title', 'summary', 'content']
    ordering_fields = ['created_at', 'updated_at', 'published_at']
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()] 