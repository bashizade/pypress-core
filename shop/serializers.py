from rest_framework import serializers
from .models import (
    Category, Product, ProductImage, ProductVariant,
    ProductAttribute, ProductAttributeValue, ShippingMethod,
    ShippingZone, Order, OrderItem, Payment, Cart, CartItem,
    Review, Chapter, Lesson, UserProgress, DiscountCode, DiscountUsage
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent', 'description']

class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = ['id', 'name', 'description']

class ProductAttributeValueSerializer(serializers.ModelSerializer):
    attribute_name = serializers.CharField(source='attribute.name', read_only=True)
    
    class Meta:
        model = ProductAttributeValue
        fields = ['id', 'attribute', 'attribute_name', 'value']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'order']

class ProductVariantSerializer(serializers.ModelSerializer):
    attributes = ProductAttributeValueSerializer(many=True, read_only=True)
    
    class Meta:
        model = ProductVariant
        fields = ['id', 'attributes', 'sku', 'price', 'sale_price', 'stock']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'id', 'title', 'description', 'content_type',
            'content', 'media_file', 'duration', 'order',
            'is_free', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class ChapterSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    
    class Meta:
        model = Chapter
        fields = [
            'id', 'title', 'description', 'order',
            'lessons', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )
    attributes = ProductAttributeValueSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    chapters = ChapterSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price',
            'product_type', 'category', 'category_id',
            'attributes', 'images', 'chapters', 'tags',
            'is_active', 'created_at', 'updated_at',
            '_meta_title', '_meta_description', '_meta_keywords'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']

class ShippingMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingMethod
        fields = ['id', 'name', 'description', 'price', 'is_active']

class ShippingZoneSerializer(serializers.ModelSerializer):
    shipping_methods = ShippingMethodSerializer(many=True, read_only=True)
    
    class Meta:
        model = ShippingZone
        fields = ['id', 'name', 'countries', 'states', 'cities', 'shipping_methods']

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        source='product'
    )
    variant = ProductVariantSerializer(read_only=True)
    variant_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductVariant.objects.all(),
        write_only=True,
        source='variant',
        required=False,
        allow_null=True
    )
    
    class Meta:
        model = OrderItem
        fields = [
            'id', 'product', 'product_id', 'variant', 'variant_id',
            'quantity', 'price', 'total'
        ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id', 'amount', 'payment_method', 'status',
            'transaction_id', 'payment_date', 'created_at'
        ]
        read_only_fields = ['created_at']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    payments = PaymentSerializer(many=True, read_only=True)
    shipping_method = ShippingMethodSerializer(read_only=True)
    shipping_method_id = serializers.PrimaryKeyRelatedField(
        queryset=ShippingMethod.objects.all(),
        write_only=True,
        source='shipping_method'
    )
    
    class Meta:
        model = Order
        fields = [
            'id', 'order_number', 'status', 'shipping_address',
            'shipping_method', 'shipping_method_id', 'shipping_cost',
            'subtotal', 'total', 'notes', 'items', 'payments',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['order_number', 'created_at', 'updated_at']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        source='product'
    )
    variant = ProductVariantSerializer(read_only=True)
    variant_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductVariant.objects.all(),
        write_only=True,
        source='variant',
        required=False,
        allow_null=True
    )
    
    class Meta:
        model = CartItem
        fields = [
            'id', 'product', 'product_id', 'variant', 'variant_id',
            'quantity', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id', 'items', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Review
        fields = [
            'id', 'product', 'user', 'rating', 'title',
            'content', 'is_approved', 'created_at'
        ]
        read_only_fields = ['user', 'is_approved', 'created_at']

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = [
            'id', 'lesson', 'is_completed', 'progress_percentage',
            'last_position', 'last_accessed', 'created_at'
        ]
        read_only_fields = ['user', 'last_accessed', 'created_at']

class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = [
            'id', 'code', 'description', 'discount_type', 'discount_value',
            'free_shipping', 'expiry_date', 'is_active', 'min_amount',
            'max_amount', 'exclude_sale_items', 'individual_use_only',
            'products', 'excluded_products', 'categories', 'excluded_categories',
            'allowed_emails'
        ]
        read_only_fields = ['id']

class DiscountUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountUsage
        fields = ['id', 'discount_code', 'user', 'order', 'used_at']
        read_only_fields = ['id', 'used_at'] 