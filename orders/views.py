from django.shortcuts import render
from .models import Order, OrderItem


# Create your views here.

def Orders(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('order_items').all()
    
    
    context = {
        'orders': orders,
    }
    
    return render(request, 'orders/orders.html', context)