# Generated by Django 5.1.2 on 2025-01-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='active_cart',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_items',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=999.99, max_digits=10),
        ),
    ]
