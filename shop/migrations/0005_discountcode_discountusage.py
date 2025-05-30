# Generated by Django 5.2.1 on 2025-05-30 09:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_merge_20250529_2331'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='کد تخفیف')),
                ('description', models.TextField(blank=True, verbose_name='توضیحات')),
                ('discount_type', models.CharField(choices=[('percentage', 'درصدی'), ('fixed_cart', 'ثابت سبد خرید'), ('fixed_product', 'ثابت محصول')], max_length=20, verbose_name='نوع تخفیف')),
                ('discount_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مقدار تخفیف')),
                ('free_shipping', models.BooleanField(default=False, verbose_name='ارسال رایگان')),
                ('expiry_date', models.DateTimeField(verbose_name='تاریخ انقضا')),
                ('usage_limit', models.PositiveIntegerField(default=0, verbose_name='حداکثر تعداد استفاده')),
                ('usage_limit_per_user', models.PositiveIntegerField(default=0, verbose_name='حداکثر تعداد استفاده برای هر کاربر')),
                ('times_used', models.PositiveIntegerField(default=0, verbose_name='تعداد دفعات استفاده')),
                ('min_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='حداقل مبلغ خرید')),
                ('max_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='حداکثر مبلغ خرید')),
                ('exclude_sale_items', models.BooleanField(default=False, verbose_name='به جز محصولات فروش ویژه')),
                ('individual_use_only', models.BooleanField(default=False, verbose_name='استفاده فردی')),
                ('allowed_emails', models.TextField(blank=True, help_text='ایمیل\u200cهای مجاز (هر خط یک ایمیل)', verbose_name='ایمیل\u200cهای مجاز')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('categories', models.ManyToManyField(blank=True, related_name='discount_codes', to='shop.category', verbose_name='دسته\u200cبندی\u200cها')),
                ('excluded_categories', models.ManyToManyField(blank=True, related_name='excluded_discount_codes', to='shop.category', verbose_name='دسته\u200cبندی\u200cهای مستثنی')),
                ('excluded_products', models.ManyToManyField(blank=True, related_name='excluded_discount_codes', to='shop.product', verbose_name='محصولات مستثنی')),
                ('products', models.ManyToManyField(blank=True, related_name='discount_codes', to='shop.product', verbose_name='محصولات')),
            ],
            options={
                'verbose_name': 'کد تخفیف',
                'verbose_name_plural': 'کدهای تخفیف',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DiscountUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ استفاده')),
                ('discount_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usages', to='shop.discountcode', verbose_name='کد تخفیف')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount_usages', to='shop.order', verbose_name='سفارش')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount_usages', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'استفاده از کد تخفیف',
                'verbose_name_plural': 'استفاده\u200cهای کد تخفیف',
                'unique_together': {('discount_code', 'order')},
            },
        ),
    ]
