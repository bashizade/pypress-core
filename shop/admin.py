from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import (
    Category, Product, ProductAttribute, ProductAttributeValue,
    ProductImage, ProductVariant, ShippingMethod, ShippingZone,
    Order, OrderItem, Payment, Cart, CartItem, Review,
    Chapter, Lesson, UserProgress, DiscountCode, DiscountUsage
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']

@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']

@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ['product', 'attribute', 'value']
    list_filter = ['attribute']
    search_fields = ['product__name', 'attribute__name', 'value']

class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 1

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'product_type', 'price', 'is_active', 'created_at']
    list_filter = ['category', 'product_type', 'is_active']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductAttributeValueInline, ProductImageInline, ChapterInline]
    
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'category', 'product_type', 'price', 'tags', 'is_active')
        }),
        ('SEO', {
            'fields': ('_meta_title', '_meta_description', '_meta_keywords'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'order']
    list_filter = ['product']
    ordering = ['product', 'order']

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ['product', 'sku', 'price', 'sale_price', 'stock']
    list_filter = ['product']
    search_fields = ['sku', 'product__name']

@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']

@admin.register(ShippingZone)
class ShippingZoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'countries']
    filter_horizontal = ['shipping_methods']
    search_fields = ['name', 'countries', 'states', 'cities']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'status', 'total', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['order_number', 'user__username']
    inlines = [OrderItemInline]
    readonly_fields = ['order_number', 'created_at', 'updated_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'variant', 'quantity', 'price', 'total']
    list_filter = ['order']
    search_fields = ['order__order_number', 'product__name']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order', 'amount', 'payment_method', 'status', 'created_at']
    list_filter = ['status', 'payment_method', 'created_at']
    search_fields = ['order__order_number', 'transaction_id']
    readonly_fields = ['created_at']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']
    search_fields = ['user__username']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'variant', 'quantity', 'created_at']
    list_filter = ['cart']
    search_fields = ['cart__user__username', 'product__name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['product__name', 'user__username', 'title', 'content']

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['product', 'title', 'order', 'created_at']
    list_filter = ['product']
    search_fields = ['product__name', 'title', 'description']
    ordering = ['product', 'order']

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'title', 'content_type', 'order', 'is_free', 'created_at']
    list_filter = ['content_type', 'is_free', 'chapter__product']
    search_fields = ['title', 'description', 'chapter__title']
    ordering = ['chapter', 'order']

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'is_completed', 'progress_percentage', 'last_accessed']
    list_filter = ['is_completed', 'lesson__chapter__product']
    search_fields = ['user__username', 'lesson__title']
    readonly_fields = ['last_accessed', 'created_at']

@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'discount_value', 'expiry_date', 'is_active', 'times_used')
    list_filter = ('discount_type', 'is_active', 'free_shipping', 'exclude_sale_items', 'individual_use_only')
    search_fields = ('code', 'description')
    readonly_fields = ('times_used', 'created_at', 'updated_at')
    filter_horizontal = ('products', 'excluded_products', 'categories', 'excluded_categories')
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('code', 'description', 'discount_type', 'discount_value', 'free_shipping', 'expiry_date', 'is_active')
        }),
        ('محدودیت‌های استفاده', {
            'fields': ('usage_limit', 'usage_limit_per_user', 'times_used')
        }),
        ('محدودیت‌های مبلغ', {
            'fields': ('min_amount', 'max_amount', 'exclude_sale_items', 'individual_use_only')
        }),
        ('محدودیت‌های محصول', {
            'fields': ('products', 'excluded_products', 'categories', 'excluded_categories')
        }),
        ('محدودیت‌های کاربر', {
            'fields': ('allowed_emails',)
        }),
        ('اطلاعات سیستمی', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(DiscountUsage)
class DiscountUsageAdmin(admin.ModelAdmin):
    list_display = ('discount_code', 'user', 'order', 'used_at')
    list_filter = ('used_at',)
    search_fields = ('discount_code__code', 'user__email', 'order__id')
    readonly_fields = ('used_at',)
