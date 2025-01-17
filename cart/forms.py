from django import forms
from .models import Cart, CartItem

class CartForm(forms.ModelForm):
    """
    Form for creating and updating a cart.
    """

    class Meta:
        model = Cart
        fields = ['user', 'active_cart', 'total_price', 'total_items']

class CartItemForm(forms.ModelForm):
    """
    Form for adding an item to a cart or updating its quantity.
    """

    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity']
