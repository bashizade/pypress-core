from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from .models import (
    Category, Product, ProductImage, ProductVariant,
    ProductAttribute, ProductAttributeValue, ShippingMethod,
    ShippingZone, Order, OrderItem, Payment, Cart, CartItem,
    Review, Chapter, Lesson, UserProgress, DiscountCode, DiscountUsage
)
from .serializers import (
    CategorySerializer, ProductSerializer, ProductImageSerializer,
    ProductVariantSerializer, ProductAttributeSerializer,
    ProductAttributeValueSerializer, ShippingMethodSerializer,
    ShippingZoneSerializer, OrderSerializer, OrderItemSerializer,
    PaymentSerializer, CartSerializer, CartItemSerializer,
    ReviewSerializer, ChapterSerializer, LessonSerializer,
    UserProgressSerializer, DiscountCodeSerializer
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.

class ProductFilter(FilterSet):
    tags = CharFilter(method='filter_tags')
    
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'product_type': ['exact'],
        }
    
    def filter_tags(self, queryset, name, value):
        return queryset.filter(tags__name__in=[value])

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name']

class ProductAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at', 'updated_at']

class ProductVariantViewSet(viewsets.ModelViewSet):
    serializer_class = ProductVariantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['sku']

    def get_queryset(self):
        return ProductVariant.objects.filter(product_id=self.kwargs['product_pk'])

class ShippingMethodViewSet(viewsets.ModelViewSet):
    queryset = ShippingMethod.objects.filter(is_active=True)
    serializer_class = ShippingMethodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

class ShippingZoneViewSet(viewsets.ModelViewSet):
    queryset = ShippingZone.objects.all()
    serializer_class = ShippingZoneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'countries', 'states', 'cities']

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status']
    ordering_fields = ['created_at', 'updated_at']
    
    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk')
        if user_pk:
            return Order.objects.filter(user_id=user_pk)
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return OrderItem.objects.filter(order_id=self.kwargs['order_pk'])

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Payment.objects.filter(order_id=self.kwargs['order_pk'])

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk')
        if user_pk:
            return Cart.objects.filter(user_id=user_pk)
        return Cart.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk')
        if user_pk:
            return CartItem.objects.filter(cart__user_id=user_pk)
        return CartItem.objects.filter(cart__user=self.request.user)
    
    def perform_create(self, serializer):
        user_pk = self.kwargs.get('user_pk')
        cart = Cart.objects.get_or_create(user_id=user_pk)[0]
        serializer.save(cart=cart)

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['rating']
    ordering_fields = ['created_at', 'rating']
    
    def get_queryset(self):
        if 'product_pk' in self.kwargs:
            return Review.objects.filter(product_id=self.kwargs['product_pk'], is_approved=True)
        return Review.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        if 'product_pk' in self.kwargs:
            product = get_object_or_404(Product, id=self.kwargs['product_pk'])
            serializer.save(user=self.request.user, product=product)
        else:
            serializer.save(user=self.request.user)

class ChapterViewSet(viewsets.ModelViewSet):
    serializer_class = ChapterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return Chapter.objects.filter(product_id=self.kwargs['product_pk'])
    
    def perform_create(self, serializer):
        product = get_object_or_404(Product, id=self.kwargs['product_pk'])
        serializer.save(product=product)

class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return Lesson.objects.filter(chapter_id=self.kwargs['chapter_pk'])
    
    def perform_create(self, serializer):
        chapter = get_object_or_404(Chapter, id=self.kwargs['chapter_pk'])
        serializer.save(chapter=chapter)

class UserProgressViewSet(viewsets.ModelViewSet):
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return UserProgress.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def update_progress(self, request, pk=None):
        progress = self.get_object()
        progress_percentage = request.data.get('progress_percentage', 0)
        last_position = request.data.get('last_position')
        
        progress.progress_percentage = progress_percentage
        if last_position:
            progress.last_position = last_position
        progress.save()
        
        return Response(self.get_serializer(progress).data)

class DiscountCodeViewSet(viewsets.ModelViewSet):
    queryset = DiscountCode.objects.all()
    serializer_class = DiscountCodeSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            return queryset.filter(is_active=True)
        return queryset

class ValidateDiscountCodeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        code = request.data.get('code')
        if not code:
            return Response({'error': 'کد تخفیف الزامی است'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            discount = DiscountCode.objects.get(code=code)
        except DiscountCode.DoesNotExist:
            return Response({'error': 'کد تخفیف نامعتبر است'}, status=status.HTTP_404_NOT_FOUND)

        if not discount.is_valid():
            return Response({'error': 'کد تخفیف منقضی شده یا غیرفعال است'}, status=status.HTTP_400_BAD_REQUEST)

        # Check user usage limit
        if discount.usage_limit_per_user > 0:
            user_usage_count = DiscountUsage.objects.filter(
                discount_code=discount,
                user=request.user
            ).count()
            if user_usage_count >= discount.usage_limit_per_user:
                return Response(
                    {'error': 'شما بیش از حد مجاز از این کد تخفیف استفاده کرده‌اید'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Check allowed emails
        if discount.allowed_emails:
            allowed_emails = discount.get_allowed_emails_list()
            if request.user.email not in allowed_emails:
                return Response(
                    {'error': 'این کد تخفیف برای ایمیل شما معتبر نیست'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Get cart total for min/max amount validation
        cart = Cart.objects.get_or_create(user=request.user)[0]
        cart_total = cart.get_total_price()

        if discount.min_amount and cart_total < discount.min_amount:
            return Response(
                {'error': f'حداقل مبلغ خرید برای استفاده از این کد تخفیف {discount.min_amount} است'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if discount.max_amount and cart_total > discount.max_amount:
            return Response(
                {'error': f'حداکثر مبلغ خرید برای استفاده از این کد تخفیف {discount.max_amount} است'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Calculate discount amount
        discount_amount = 0
        if discount.discount_type == 'percentage':
            discount_amount = (cart_total * discount.discount_value) / 100
        elif discount.discount_type == 'fixed_cart':
            discount_amount = discount.discount_value
        elif discount.discount_type == 'fixed_product':
            # Calculate for each eligible product
            for item in cart.items.all():
                if (not discount.products.exists() or item.product in discount.products.all()) and \
                   (not discount.excluded_products.exists() or item.product not in discount.excluded_products.all()) and \
                   (not discount.categories.exists() or item.product.category in discount.categories.all()) and \
                   (not discount.excluded_categories.exists() or item.product.category not in discount.excluded_categories.all()) and \
                   (not discount.exclude_sale_items or not item.product.is_on_sale):
                    discount_amount += discount.discount_value * item.quantity

        return Response({
            'code': discount.code,
            'discount_type': discount.discount_type,
            'discount_value': discount.discount_value,
            'discount_amount': discount_amount,
            'free_shipping': discount.free_shipping
        })
