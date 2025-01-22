from django.contrib import admin
from .models import Category, Product, Tag

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    filter_horizontal = ('tags',)

    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)