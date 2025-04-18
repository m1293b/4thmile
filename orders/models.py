from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Order(models.Model):
    """
    Represents an order in the database.

    Attributes:
        total (float): The total cost of the order.
        status (str): The status of the order (e.g. "pending", "shipped", etc.).
        created_at (datetime): The date and time the order was created.
        updated_at (datetime): The date and time the order was last updated.
        notes (str): Any additional notes about the order.
        user (User): The user who placed the order.
        email (EmailField): The user's email address.


    Returns:
        str: A string representation of the order.
    """

    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} for {self.user}"


class OrderItem(models.Model):
    """
    Represents an item in an order in the database.

    Attributes:
        order (Order): The order that this item belongs to.
        price (float): The price of the product.
        product (Product): The product that this item represents.
        quantity (int): The quantity of the product ordered.
        created_at (datetime): The date and time the order item was created.
        updated_at (datetime): The date and time the order item was last updated.

    Returns:
        str: A string representation of the order item.
    """

    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_items"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
