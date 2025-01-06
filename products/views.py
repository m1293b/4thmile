from django.shortcuts import get_object_or_404, render
from .models import Product, Category, ProductImage

# Create your views here.

def Products(request):
    
    products = (
        Product.objects
        .select_related('category')  # Optimize category access
        .prefetch_related(
            'productimage_set',  # Prefetch related product images
        )
        .all()
    )
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    
    return render(request, './products/products.html')

def Clothes(request):
    
    clothes = Product.objects.filter(Category.objects.filter(name='Clothes').all()) # does this work?
    clothes_categories = Category.objects.filter(main_category='Clothes').all()
    context = {
        'clothes': clothes,
        'categories': clothes_categories
    }
    return render(request, '/products/clothes.html', context)

def product_detail(request, pk):
    
    product = get_object_or_404(Product, pk=pk)
    
    context = {
        'product': product,
    }
    
    return render(request, './products/product_detail.html', context)