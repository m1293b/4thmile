from django.db import models
from products.models import Product
from accounts.models import Customer

# Create your models here.

class Order(models.Model):
    """
    Represents an order in the database.

    Attributes:
        order_id (int): A unique identifier for the order.
        customer (Customer): The customer who placed the order.
        order_date (date): The date the order was placed.
        total (float): The total cost of the order.
        status (str): The status of the order (e.g. "pending", "shipped", etc.).
        created_at (datetime): The date and time the order was created.
        updated_at (datetime): The date and time the order was last updated.
        notes (str): Any additional notes about the order.

    Returns:
        str: A string representation of the order.
    """
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Order {self.id} for {self.customer}"

class OrderItem(models.Model):
    """
    Represents an item in an order in the database.

    Attributes:
        order_item_id (int): A unique identifier for the order item.
        order (Order): The order that this item belongs to.
        price (float): The price of the product.
        product (Product): The product that this item represents.
        quantity (int): The quantity of the product ordered.
        created_at (datetime): The date and time the order item was created.
        updated_at (datetime): The date and time the order item was last updated.

    Returns:
        str: A string representation of the order item.
    """
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"