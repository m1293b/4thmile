from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, ProductImage
from .forms import ProductForm, ProductImageForm

# Create your views here.


def products(request):
    """
    This function is used to display all the products in the database. It also allows users to search for products by name or category.
    """

    products = (
        Product.objects.select_related("category")
        .prefetch_related(
            "productimage_set",
        )
        .all()
    )

    categories = Category.objects.all()

    query = None

    page_title = "View Products"
    page_description = "View all the products available in our store."

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "Please enter a search term.")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(category__name__icontains=query)
            products = products.filter(queries)
            page_title = f"Search Results: {query}"
            page_description = f"View all the products available in our store that match your search term '{query}'."

    context = {
        "products": products,
        "categories": categories,
        "search_term": query,
        "page_title": page_title,
        "page_description": page_description,
    }

    return render(request, "products/products.html", context)


def add_product(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)

        if product_form.is_valid() and image_form.is_valid():
            product_instance = product_form.save()

            # Handle multiple images
            for file in request.FILES.getlist("image"):
                image_instance = image_form.save(commit=False)
                image_instance.product = product_instance
                image_instance.image = file
                image_instance.save()

            return redirect(
                "productdetail"
            )  # Replace with your actual view name or URL

    else:
        product_form = ProductForm()
        image_form = ProductImageForm()

    context = {
        "product_form": product_form,
        "image_form": image_form,
    }

    return render(request, "products/add_product.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
