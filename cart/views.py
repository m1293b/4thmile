from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .cart import Cart
from products.models import Product
from .forms import CartForm, CartItemForm


# Create your views here.


def cart_summary(request):
    
    # Logic to retrieve and display the cart items
    
    return render(request, "cart/cart_summary.html")


def add_to_cart(request):
    # Logic to add a product to the cart
    pk = int(request.POST.get('product_id'))
    cart = Cart(request)
    
    if request.POST:
        product = get_object_or_404(Product,pk=pk)
        quantity = int(request.POST.get('quantity'))
        print(product)
        print(quantity)
        
        cart.add(product=product, quantity=quantity)    
        messages.success(request, f"{product.name} added to cart.")
        
    return JsonResponse({'status': 'success'})


def update_cart(request, product_id, quantity):
    # Logic to update the quantity of a product in the cart
    return render(request, "cart/cart.html")


def remove_from_cart(request, product_id):
    # Logic to remove a product from the cart
    return render(request, "cart/cart.html")


def checkout(request):
    # Logic for handling the checkout process
    return render(request, "cart/checkout.html")


def order_summary(request):
    # Logic to display the summary of an order
    return render(request, "cart/order_summary.html")
