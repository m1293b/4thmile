from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .cart import Cart as cart_session
from products.models import Product
from .models import Cart, CartItem
from .forms import CartForm, CartItemForm


# Create your views here.


def cart_summary(request):
    
    # Logic to retrieve and display the cart items
    
    return render(request, "cart/cart_summary.html")


def add_to_cart(request):
    # Logic to add a product to the cart
    pk = int(request.POST.get('product_id'))
    cart_sess = cart_session(request)

    if request.POST:

        product = get_object_or_404(Product,pk=pk)
        quantity = int(request.POST.get('quantity'))

        if request.user.is_authenticated:
            try:
                cart, created = Cart.objects.get_or_create(
                    user=request.user,
                    active_cart=True
                )

                # Update or create items in this cart based on session data
                for item_id, quantity in request.session.get('cart', {}).items():
                    product = Product.objects.get(pk=item_id)

                    # Try to get an existing cart item, otherwise create a new one
                    cart_item, created = CartItem.objects.get_or_create(
                        cart=cart,
                        product=product
                    )

                    # Update the quantity if it already exists or set it for new items
                    if not created:
                        cart_item.quantity += quantity
                    else:
                        cart_item.quantity = quantity

                    # Save changes to the cart item
                    cart_item.save()

                # Recalculate total price and items in the cart
                cart.total_price = sum(item.product.price * item.quantity for item in cart.items.all())
                cart.total_items = sum(item.quantity for item in cart.items.all())
                cart.save()

            except Cart.DoesNotExist:
                # Create a new active cart if none exists
                cart = Cart.objects.create(
                    user=request.user,
                    active_cart=True,
                    total_price=0.00,
                    total_items=0
                )

        cart_sess.add(product=product, quantity=quantity)

        cart_len = cart_sess.__len__()
        
        message = f"{product.name} added to cart."

    return JsonResponse({"cart_len":cart_len, "message": message,})


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
