from django.contrib import admin
from .models import Category, Product, ProductImage

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)