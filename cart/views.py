from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .cart import Cart as cart_session
from products.models import Product
from .models import Cart, CartItem
from accounts.models import Customer


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
    if not pk:
        # Handle error: return a response indicating failure
        return JsonResponse({"error": "Product ID is required"}, status=400)
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

                # Update or create each cart item with the correct quantity
                for item_id, quantity_data in cart_sess.cart.items():
                    product = Product.objects.get(pk=item_id)
                    quantity = int(quantity_data["quantity"])

                    cart_item, created = CartItem.objects.update_or_create(
                        cart=cart, product=product, defaults={"quantity": quantity}
                    )

                # Recalculate total price and items in the cart
                cart.total_price = float(
                    sum(
                        (
                            item.product.sale_price
                            if item.product.is_on_sale
                            else item.product.price
                        )
                        * item.quantity
                        for item in cart.items.all()
                    )
                )
                cart.total_items = sum(item.quantity for item in cart.items.all())
                cart.save()

            except Cart.DoesNotExist:
                # Handle case where active cart doesn't exist, if applicable
                pass

        cart_len = len(cart_sess)

        return JsonResponse(
            {
                "cart_len": cart_len,
                "message": message,
            }
        )
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
    pk = int(request.POST.get("product_id"))
    new_quantity = int(request.POST.get("quantity"))

    # Retrieve the session cart
    cart_sess = cart_session(request)
    if str(pk) in cart_sess.cart:
        current_product = Product.objects.get(pk=pk)

        # Check stock availability
        if new_quantity <= current_product.stock:
            cart_sess.update(product=current_product, quantity=new_quantity)
            message = f"Quantity updated to {new_quantity} for {current_product.name}."
            if new_quantity == 0:
                cart_sess.remove(product=current_product)
                message = f"{current_product.name} removed from the cart."
        else:
            # Add only as much as the available stock allows
            total_quantity = current_product.stock
            cart_sess.update(product=current_product, quantity=total_quantity)
            message = f"Added {current_product.stock} to reach maximum available stock for {current_product.name}."
    else:
        message = "Product not found in the cart."

    # Update database cart for authenticated users
    if request.user.is_authenticated:
        try:
            cart, created = Cart.objects.get_or_create(
                user=request.user, active_cart=True
            )

            product = Product.objects.get(pk=pk)
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart, product=product
            )

            # Calculate the new total quantity after update
            current_quantity = cart_item.quantity

            # Determine how much to add based on available stock
            if str(pk) in cart_sess.cart:
                max_addable = product.stock - current_quantity
                final_quantity = min(new_quantity, current_quantity + max_addable)

                if final_quantity > 0 and max_addable >= 0:
                    # Update or set the quantity of the cart item
                    cart_item.quantity = final_quantity
                    message = (
                        f"Quantity updated to {final_quantity} for {product.name}."
                    )
                else:
                    message = "Cannot exceed available stock."

            # Save the changes to the cart item
            cart_item.save()

            # Recalculate total price and items in the cart
            cart.total_price = sum(
                item.product.price * item.quantity for item in cart.items.all()
            )
            cart.total_items = sum(item.quantity for item in cart.items.all())
            cart.save()

        except Cart.DoesNotExist:
            pass

    cart_len = len(cart_sess)

    return JsonResponse(
        {
            "cart_len": cart_len,
            "message": message,
            "total": round(cart_sess.cart[str(product.pk)]["total"], 2),
        }
    )


def remove_from_cart(request):

    cart_sess = cart_session(request)
    product_id = int(request.POST.get("product_id"))
    product = Product.objects.filter(pk=product_id).first()
    removed_items_num = int(request.POST.get("quantity"))

    # Removing product from session.cart
    cart_sess.remove(product)
    cart_len = cart_sess.__len__()

    # Removing product from database if found
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
    cart_sess.clear(request)
    return JsonResponse(
        {
            "message": "All carts, cart items, and the session cart have been cleared successfully."
        }
    )


# Allow users without an account to checkout
def checkout(request):
    user = request.user if request.user.is_authenticated else None
    cart_sess = cart_session(request)

    # If no user, get the session cart instead
    if not user:
        cart_sess = cart_session(request)
    else:
        customer, created = Customer.objects.get_or_create(user=user)

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email") or (user.email if user else None)
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")

        # Create a new customer if not authenticated
        if not user:
            customer, created = Customer.objects.get_or_create(email=email)

        if created:
            customer.first_name = first_name
            customer.last_name = last_name
            customer.email = email
            customer.phone_number = phone_number
            customer.address = address

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
            "customer": customer,
        }
        # Redirect to payment processing view after saving shipping details
        return redirect("process_payment")

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
        "customer": customer if user else cart_sess,
        "cart_total": cart_sess.get_total(),
    }
    return render(request, "cart/checkout.html", context)
