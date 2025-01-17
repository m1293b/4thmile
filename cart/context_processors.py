from .cart import Cart


def cart(request):
    return {"cart": Cart(request)}

def cart_total_items(request):
    cart = request.session.get('cart', {})
    print(cart)
    total_items = sum(item['quantity'] for item in cart.values())
    return {'total_items': total_items}