from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ReviewForm


def Reviews(request):
    return render(request, "reviews.html")


@login_required
def add_review(request, pk):
    product = get_object_or_404(Product, pk=pk)

    reviews = Review.objects.filter(product=product)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Review added successfully!")
            return redirect("product_detail", pk=pk)
        else:
            for field_name, error_messages in form.errors.items():
                if isinstance(error_messages, list):
                    for message in error_messages:
                        full_message = f"{form.fields[field_name].label}: {message}"
                        messages.error(request, full_message)
                else:
                    full_message = f"{form.fields[field_name].label}: {error_messages}"
                    messages.error(request, full_message)

    else:
        form = ReviewForm()

    context = {
        "product": product,
        "reviews": reviews,
    }

    return render(request, "products/product_detail.html", context)


def review_list(request):
    reviews = Review.objects.all()
    return render(request, "reviews/review_list.html", {"reviews": reviews})
