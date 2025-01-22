from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from products.models import Product


class Cart(models.Model):
    """
    Represents a cart in the database.

    Attributes:
        cart_id (int): A unique identifier for the cart.
        user (User): The user who owns the cart.
        created_at (datetime): The date and time the cart was created.
        updated_at (datetime): The date and time the cart was last updated.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    active_cart = models.BooleanField(default=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=999.99)
    total_items = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    """
    Represents an item in a cart in the database.

    Attributes:
        cart (Cart): The cart that this item belongs to.
        product (Product): The product that this item represents.
        quantity (int): The quantity of the product ordered.
        created_at (datetime): The date and time the cart item was created.
        updated_at (datetime): The date and time the cart item was last updated.

    Returns:
        str: A string representation of the cart item.
    """

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
