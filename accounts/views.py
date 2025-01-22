import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Customer
from cart.models import CartItem

stripe.api_key = settings.STRIPE_SECRET_KEY

def process_payment(request):
    user = request.user
    cart_items = CartItem.objects.filter(cart__user=user)

    # Calculate total amount
    amount = sum(item.total for item in cart_items) * 100

    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        customer_email = request.POST.get('email', user.email)

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description=f'Charge for {customer_email}',
                source=token
            )
            # On successful payment, transfer items to the the order model, clear the cart and redirect to a success page.
            CartItem.objects.filter(cart__user=user).delete()
            return render(request, 'cart/payment_success.html')
        except stripe.error.StripeError as e:
            return render(request, 'cart/checkout.html', {'error': str(e)})

    context = {
        'total_amount': amount / 100,  # Convert back to dollars for display
        'stripe_key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'cart/process_payment.html', context)

# Do we get the stripe payment reference number back?