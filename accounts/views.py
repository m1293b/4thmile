import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Customer
from cart.models import Cart, CartItem

stripe.api_key = settings.STRIPE_SECRET_KEY


def process_payment(request):
    user = request.user

    # Get the user's cart or create a new one if it doesn't exist
    try:
        cart, created = Cart.objects.get_or_create(user=user)
    except Cart.DoesNotExist:
        return render(request, "cart/checkout.html", {"error": "Cart not found."})

    # Retrieve total amount from the Cart model
    amount = cart.total_price * 100  # Convert pounds to pence

    if request.method == "POST":
        token = request.POST.get("stripeToken")
        customer_email = request.POST.get("email", user.email)

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="gbp",
                description=f"Charge for {customer_email}",
                source=token,
            )

            # Optionally store the payment intent or charge ID if needed
            payment_reference = charge.id

            # On successful payment, clear the cart and redirect to a success page.
            cart_items = CartItem.objects.filter(cart=cart)
            cart_items.delete()

            return render(
                request,
                "cart/payment_success.html",
                {"payment_reference": payment_reference},
            )

        except stripe.error.StripeError as e:
            error_message = str(e)
            print(f"Stripe Error: {error_message}")

            if isinstance(e, stripe.error.CardError):
                error_message = "Your card was declined."
            elif isinstance(e, stripe.error.RateLimitError):
                error_message = "Rate limit error. Please try again later."
            elif isinstance(e, stripe.error.InvalidRequestError):
                error_message = "Invalid parameters were supplied to Stripe."
            elif isinstance(e, stripe.error.AuthenticationError):
                error_message = "Authentication with Stripe's API failed."
            elif isinstance(e, stripe.error.APIConnectionError):
                error_message = "Network communication with Stripe failed."
            else:
                error_message = "An unknown error occurred."

            return render(request, "cart/checkout.html", {"error": error_message})

    context = {
        "total_amount": cart.total_price,  # Display total in pounds
        "stripe_key": settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, "accounts/process_payment.html", context)
