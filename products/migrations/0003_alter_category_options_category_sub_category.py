# Generated by Django 5.1.2 on 2024-12-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_productimage_sales_product_is_on_sale_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
