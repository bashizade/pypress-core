from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0002_remove_attributes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(through='shop.ProductAttributeValue', to='shop.productattribute'),
        ),
    ] 