# Generated by Django 5.1.2 on 2024-12-31 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_options_category_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]