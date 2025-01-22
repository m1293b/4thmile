# Generated by Django 5.1.2 on 2025-01-21 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('friendly_name', models.CharField(blank=True, max_length=100)),
                ('main_category', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New product', max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products/images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('color', models.CharField(blank=True, max_length=50)),
                ('size', models.CharField(blank=True, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True)),
                ('smiles', models.IntegerField(default=0)),
                ('purchases', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('sales', models.IntegerField(default=0)),
                ('is_on_sale', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(decimal_places=2, default=999, max_digits=10)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('tags', models.ManyToManyField(related_name='products', to='products.tag')),
            ],
        ),
    ]
