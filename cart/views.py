from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .cart import Cart as cart_session
from products.models import Product
from .models import Cart, CartItem


def cart_summary(request):
    # Logic to retrieve and display the cart items
    cart_sess = cart_session(request)

    # Ensure get_cart_items returns a list of dictionaries with all required details
    cart_products = [
        {
            "product": product,
            "quantity": cart_sess.cart[str(product.pk)]["quantity"],
            "total": cart_sess.cart[str(product.pk)]["total"],
        }
        for product in cart_sess.get_cart_items()
    ]

    context = {
        "cart_products": cart_products,
    }

    return render(request, "cart/cart_summary.html", context)

def add_to_cart(request):
    pk = int(request.POST.get("product_id"))
    cart_sess = cart_session(request)
    if request.POST:
        product = get_object_or_404(Product, pk=pk)
        quantity = int(request.POST.get("quantity"))

        # Add to session cart
        if not cart_sess.add(product=product, quantity=quantity):
            message = "Cannot add more than the available stock."
        else:
            message = f"{quantity}x {product.name} added to cart."

        # Update database cart for authenticated users
        if request.user.is_authenticated:
            try:
                cart, created = Cart.objects.get_or_create(
                    user=request.user, active_cart=True
                )
                
                for item_id, quantity_data in cart_sess.cart.items():
                    product = Product.objects.get(pk=item_id)
                    cart_item, created = CartItem.objects.get_or_create(
                        cart=cart, product=product, quantity=quantity_data["quantity"]
                    )
                    
                    # Update or set the quantity of the cart item
                    if not created:
                        cart_item.quantity += int(quantity_data["quantity"])
                    else:
                        cart_item.quantity = int(quantity_data["quantity"])

                    cart_item.save()

                # Recalculate total price and items in the cart
                cart.total_price = sum(
                    item.product.price * item.quantity for item in cart.items.all()
                )
                cart.total_items = sum(item.quantity for item in cart.items.all())
                cart.save()

            except Cart.DoesNotExist:
                # Handle case where active cart doesn't exist, if applicable
                pass

        cart_len = len(cart_sess)
    else:
        message = "No POST data received."
        cart_len = 0

    return JsonResponse(
        {
            "cart_len": cart_len,
            "message": message,
        }
    )

def update_cart(request):
    # Logic to update the quantity of a product in the cart
    return render(request, "cart/cart.html")


def remove_from_cart(request):

    cart_sess = cart_session(request)
    product_id = int(request.POST.get("product_id"))
    product = Product.objects.filter(pk=product_id).first()
    removed_items_num = int(request.POST.get("quantity"))

    # Removing product from session.cart
    cart_sess.remove(product)
    cart_len = cart_sess.__len__()

    # Removing product from database
    try:
        for cart_item in CartItem.objects.filter(product=product_id):
            cart_item.delete()
    except Product.DoesNotExist as e:
        print(f"Product {product_id} not found in CartItem database.")

    message = f"{removed_items_num}x {product.name} removed from cart."

    return JsonResponse(
        {
            "cart_len": cart_len,
            "message": message,
        }
    )


@login_required
def clear_all_carts(request):
    # Get all carts for the logged-in user
    user_carts = Cart.objects.filter(user=request.user)

    # Delete all associated CartItems first to maintain integrity
    for cart in user_carts:
        CartItem.objects.filter(cart=cart).delete()

    # Then delete the Carts themselves
    user_carts.delete()

    # Clear session cart if it exists
    cart_sess = cart_session(request)
    cart_sess.clear(request)  # Ensure method is called correctly with `request`
    return JsonResponse(
        {
            "message": "All carts, cart items, and the session cart have been cleared successfully."
        }
    )


def checkout(request):
    # Logic for handling the checkout process
    return render(request, "cart/checkout.html")


def order_summary(request):
    # Logic to display the summary of an order
    return render(request, "cart/order_summary.html")
