from django.http import JsonResponse
from django.shortcuts import render
from cart.models import Cart, CartItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "home/home.html")


@login_required
def profile(request):

    carts = Cart.objects.filter(user=request.user).all()

    if not carts:
        messages.success(request, "You do not have a cart.")
        cart_items = []
    else:
        # Fetch all items from the selected carts
        cart_items = [
            item
            for cart in carts
            for item in CartItem.objects.filter(cart=cart).select_related("product")
        ]

        if not cart_items:
            messages.success(request, "Cart exists but no items found for this cart.")
        else:
            messages.success(request, f"These are the items in your cart")

    context = {
        "carts": carts,
        "cart_items": cart_items,
    }

    return render(request, "home/profile.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
