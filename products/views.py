from django.shortcuts import render
from .models import Product, Category, ProductImage

# Create your views here.

def Products(request):
    
    products = Product.objects.all()
    categories = Category.objects.all()
    product_images = ProductImage.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'product_images': product_images
    }
    
    return render(request, '/products/products.html')

def Clothes(request):
    
    clothes = Product.objects.filter(Category.objects.filter(name='Clothes').all()) # does this work?
    clothes_categories = Category.objects.filter(name='Clothes').all()
    context = {
        'clothes': clothes,
        'categories': clothes_categories
    }
    return render(request, '/products/clothes.html', context)