import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from cart.cart import Cart as cart_sess
from orders.models import Order, OrderItem
from cart.models import Cart, CartItem
from .forms import CustomPasswordChangeForm
from .models import Customer


def process_payment(request):

    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key
    stripe_payment_intent = stripe.PaymentIntent.create(
        amount=round(cart_sess(request).get_total() * 100) if round(cart_sess(request).get_total() * 100) > 50 else 50,  # Amount in cents
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
    user = request.user if request.user.is_authenticated else None
    cart_session = cart_sess(request)
    order = None

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
                    price=item.product.sale_price if item.product.is_on_sale else item.product.price,
                    quantity=item.quantity,
                )
                order_item.save()
                item.delete()  # Delete the items from the cart after processing
            cart.delete()
            order = Order.objects.filter(user=request.user).order_by("-created_at")[:1]
    else:
        order = Order.objects.create(
            user=None, status="Shipped", total=cart_session.get_total()
        )
        cart_items = [item for item in cart_session.cart.values()]
        for item in cart_items:
            order_item = OrderItem(
                order=order,
                product=Product.objects.filter(pk=int(item["id"])).first(),
                price=float(item["total"]),
                quantity=int(item["quantity"]),
            )
            order_item.save()
            order = Order.objects.filter(user=None).order_by("-created_at")[:1]

    cart_session.clear(request)  # Delete the cart session after payment is successful
    order_items = OrderItem.objects.filter(order=order).all()

    context = {
        "orderz": order,
        "order_items": order_items,
    }

    messages.success(request, "Payment successful! Your order has been processed.")
    return render(request, "accounts/success.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        user = request.user
        
        account, created = Customer.objects.get_or_create(user=user, email=request.POST.get("email"))
        password_form = CustomPasswordChangeForm(
            user=request.user, data=request.POST or None
        )

        username = (
            request.POST.get("username") if request.POST.get("username") else None
        )
        email = request.POST.get("email") if request.POST.get("email") else None
        first_name = request.POST.get("first_name")
        last_name = (
            request.POST.get("last_name") if request.POST.get("last_name") else None
        )
        phone_number = (
            request.POST.get("phone_number")
            if request.POST.get("phone_number")
            else None
        )
        address = request.POST.get("address") if request.POST.get("address") else None
        notes = request.POST.get("notes") if request.POST.get("notes") else None

        user.username = username if username else user.username
        user.email = email if email else user.email
        user.first_name = first_name if first_name else user.first_name
        user.last_name = last_name if last_name else user.last_name
        user.save()

        messages.success(request, "User details updated successfully.")
        
        account.user = request.user
        account.username = username if username else account.username
        account.first_name = first_name if first_name else account.first_name
        account.last_name = last_name if last_name else account.last_name
        account.phone_number = phone_number if phone_number else account.phone_number
        account.address = address if address else account.address
        account.notes = notes if notes else account.notes
        account.save()

        messages.success(request, "Customer details updated successfully.")

    else:
        try:
            user = request.user
            account = Customer.objects.get(user=user)
        except Customer.DoesNotExist:
            account = None
            messages.error(request, 'Please update cutomer details.')
        password_form = CustomPasswordChangeForm(
            user=request.user, data=request.POST or None
        )

    context = {
        "user": user,
        "account": account,
        "password_form": password_form,
    }
    return render(request, "accounts/profile.html", context)


def update_password(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            new_password1 = form.cleaned_data.get("new_password1")
            new_password2 = form.cleaned_data.get("new_password2")
            if new_password1 != new_password2:
                messages.error(
                    request,
                    "Passwords do not match. Please try again.",
                )
                return render(request, "accounts/change_password.html", {"form": form})
            form.save()
            messages.success(request, "Password changed successfully.")
            return redirect("profile")
        else:
            messages.error(
                request,
                "Please correct the errors in the form.",
            )

    return redirect("profile")
