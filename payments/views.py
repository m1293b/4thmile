import stripe
import os
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from .models import Payment
from orders.models import Order, OrderItem

# Create your views here.

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

class StripeCheckoutView(View):
    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)
        total_amount = sum(item.price * item.quantity for item in order_items)

        try:
            # Create a Stripe payment intent
            payment_intent = stripe.PaymentIntent.create(
                amount=int(total_amount * 100),  # convert to cents
                currency='usd',
                payment_method_types=['card'],
            )

            # Create a Stripe checkout session
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'Order #{}'.format(order.id),
                            },
                            'unit_amount': int(total_amount * 100),  # convert to cents
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url='http://example.com/success',
                cancel_url='http://example.com/cancel',
            )

            return redirect(checkout_session.url)
        except stripe.error.CardError as e:
            return JsonResponse({'error': str(e)})

    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        payment_method = request.POST.get('payment_method')
        payment_intent = request.POST.get('payment_intent')

        try:
            # Create a Payment instance
            payment = Payment.objects.create(
                order=order,
                payment_method=payment_method,
                payment_intent=payment_intent,
            )

            # Update the order status
            order.status = 'paid'
            order.save()

            return JsonResponse({'message': 'Payment successful'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
