from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from .models import Product, Category, ProductImage
from .forms import ProductForm, ProductImageForm
from reviews.forms import ReviewForm
from reviews.models import Review
from django.contrib import messages

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

    categories = Category.objects.prefetch_related(
        "product_set",
    ).all()

    main_category = None
    category = None

    query = None
    sort = None
    products_list = []

    page_title = "View Products"
    page_description = "View all the products available in our store."

    if request.GET:

        if "main_category" in request.GET:
            main_category = request.GET["main_category"]
            products = products.filter(category__main_category=main_category)
            # if main_category:
            #     categories = categories.filter(main_category=main_category)
            #     for category_sub in categories:
            #         if category_sub.main_category == main_category:
            #             products.append(category_sub)
            page_title = f"Products in main category: {main_category}"
            page_description = f"View all the products available in our store that belong to the main category '{main_category}'."

        if "category" in request.GET:
            category_name = request.GET["category"]
            products = products.filter(category__friendly_name=category_name)
            category = categories.filter(friendly_name=category_name).first()
            page_title = f"Products in category: {category.friendly_name}"
            page_description = f"View all the products available in our store that belong to the category '{category.friendly_name}'."

        if "q" in request.GET:
            query = request.GET["q"]
            queries = Q(name__icontains=query) | Q(category__name__icontains=query)
            products = products.filter(queries)
            page_title = f"Search Results: {query}"
            page_description = f"View all the products available in our store that match your search term '{query}'."

        if "sort" in request.GET:
            sort = request.GET.get("sort", "")
            # Ensure safe sorting by checking valid fields
            valid_sort_fields = [
                "name",
                "-name",
                "price",
                "-price",
            ]  # Add more as needed
            if sort in valid_sort_fields:
                products = products.order_by(sort)
            else:
                sort = ""  # Reset to default if invalid

    context = {
        "products": products,
        "main_category": main_category,
        "category": category,
        "search_term": query,
        "sort": sort,
        "page_title": page_title,
        "page_description": page_description,
    }

    return render(request, "products/products.html", context)


def add_product(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        image_form = ProductImageForm(request.FILES)

        if product_form.is_valid() and image_form.is_valid():
            product_instance = product_form.save()

            # Handle multiple images
            for file in request.FILES.getlist("image"):
                image_instance = image_form.save(commit=False)
                image_instance.product = product_instance
                image_instance.image = file
                image_instance.save()

            messages.success(request, "Product added successfully!")
            return redirect("product_detail", pk=product_instance.pk)

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
    reviews = Review.objects.filter(product=product).order_by("-created_at")[:3]

    context = {
        "product": product,
        "reviews": reviews,
    }

    return render(request, "products/product_detail.html", context)


# def add_to_cart(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     cart_item, created_at = CartItem.objects.get_or_create(
#         user=request.user, product=product
#     )
#     cart_item.quantity += 1
#     cart_item.save()
#     return redirect("cart")  # Redirect to the cart page
