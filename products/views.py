from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Category, ProductImage
from .forms import ProductForm, ProductImageForm

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

def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)

        if product_form.is_valid() and image_form.is_valid():
            product_instance = product_form.save()

            # Handle multiple images
            for file in request.FILES.getlist('image'):
                image_instance = image_form.save(commit=False)
                image_instance.product = product_instance
                image_instance.image = file
                image_instance.save()
            
            return redirect('product_list')  # Replace with your actual view name or URL

    else:
        product_form = ProductForm()
        image_form = ProductImageForm()

    context = {
        'product_form': product_form,
        'image_form': image_form,
    }
    
    return render(request, 'products/add_product.html', context)