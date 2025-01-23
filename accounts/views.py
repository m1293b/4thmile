import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from cart.cart import Cart as cart_sess
from orders.models import Order, OrderItem
from cart.models import Cart, CartItem
from .forms import UserUpdateForm


def process_payment(request):

    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key
    stripe_payment_intent = stripe.PaymentIntent.create(
        amount=round(cart_sess(request).get_total() * 100),  # Amount in cents
        currency="gbp",
        payment_method_types=["card"],
        # metadata={"session_id": cart_sess.session_id},
    )

    try:
        cart_session = cart_sess(request)
    except Cart.DoesNotExist:
        return render(request, "cart/checkout.html", {"error": "Cart not found."})

    context = {
        "total_amount": round(
            cart_session.get_total() * 100
        ),  # Display total in pounds
        "to_pay": cart_session.get_total(),
        "stripe_public_key": stripe_publishable_key,
        "client_secret": stripe_payment_intent.client_secret,
    }
    return render(request, "accounts/process_payment.html", context)


def success(request):

    user = request.user or None
    cart_sess = cart_sess(request)

    if user:
        cart = Cart.objects.filter(user=user).first()
        if cart:
            order = Order.objects.create(
                user=user, status="Shipped", total=cart.total_price
            )
            cart_items = CartItem.objects.filter(cart=cart).all()
            for item in cart_items:
                order_item = OrderItem(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity,
                )
                order_item.save()
                item.delete()  # Delete the items from the cart after processing
            cart.delete()
    else:
        order = Order.objects.create(
            user=None, status="Shipped", total=cart_sess.get_total()
        )
        cart_items = [int(item) for item in cart_sess.items.keys()]
        for item in cart_items:
            order_item = OrderItem(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity,
            )
            order_item.save()
            item.delete()  # Delete the items from the cart after processing

    cart_sess.delete()  # Delete the cart session after payment is successful

    messages.success(request, "Payment successful! Your order has been processed.")
    return render(request, "accounts/success.html")


def profile(request):
    user_form = None
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {
        "user_form": user_form,
    }
    return render(request, "accounts/profile.html", context)
