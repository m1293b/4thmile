from django.shortcuts import get_object_or_404, render
from django.db.models import Q, Prefetch
from .models import Product, Category
from reviews.models import Review


def products(request):
    """
    This function is used to display all the products in the database. It also allows users to search for products by name or category.
    """

    # Define base queryset for products with potential sorting applied later
    product_queryset = Product.objects.all()

    main_category = None
    categories = Category.objects.all()  # Initialize categories

    query = None
    sort = request.GET.get("sort", "")

    page_title = "View Products"
    page_description = "View all the products available in our store."

    if request.GET:

        if "main_category" in request.GET:
            main_category = request.GET["main_category"]
            categories = (
                Category.objects.prefetch_related(
                    Prefetch("product_set", queryset=product_queryset)
                )
                .all()
                .filter(main_category=main_category)
            )
            page_title = f"Products in main category: {main_category}"
            page_description = f"View all the products available in our store that belong to the main category '{main_category}'."

        if "category" in request.GET:
            category_name = request.GET["category"]
            categories = (
                Category.objects.prefetch_related(
                    Prefetch("product_set", queryset=product_queryset)
                )
                .all()
                .filter(friendly_name=category_name)
            )
            page_title = f"Products in category: {categories.first().friendly_name}"
            page_description = f"View all the products available in our store that belong to the category '{categories.first().friendly_name}'."

        if "q" in request.GET:
            query = request.GET["q"]
            page_title = f"Search result for '{query}'"
            page_description = ""
            # Corrected filtering on Product fields
            product_queryset = product_queryset.filter(
                Q(name__icontains=query)
                | Q(category__name__icontains=query),
            ).filter(stock__gt=0)  # Assuming 'stock' is the field you want to filter by

            categories = categories.prefetch_related(
                Prefetch("product_set", queryset=product_queryset)
            )

        # Prepare a sorted product queryset only if valid sort parameter is provided
        valid_sort_fields = ["name", "-name", "price", "-price"]
        if sort in valid_sort_fields:
            product_queryset = product_queryset.order_by(sort)
            page_description += f" Sorted by {sort}"

    products_found = any(category.product_set.exists() for category in categories)

    # Apply the potentially sorted product queryset to prefetch_related

    context = {
        "products_found": products_found,
        "categories": categories,
        "main_category": main_category,
        "search_term": query,
        "sort": sort,
        "page_title": page_title,
        "page_description": page_description,
    }

    return render(request, "products/products.html", context)

def add_product(request):
    """
    This view is used to display the form for adding a new product.
    """

    return render(request, "products/add_product.html")


def product_detail(request, pk):
    """
    This view displays the details of a specific product based on its primary key (pk).
    """

    product = get_object_or_404(Product, pk=pk)
    reviews = Review.objects.filter(product=product).order_by("-created_at")[:3]

    context = {
        "product": product,
        "reviews": reviews,
    }

    return render(request, "products/product_detail.html", context)
