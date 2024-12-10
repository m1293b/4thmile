from django.db import models
from orders.models import Order

# Create your models here.

class ShippingAddress(models.Model):
    """
    Represents a shipping address in the database.

    Attributes:
        order (Order): The order that this shipping address belongs to.
        address_line_1 (str): The first line of the shipping address.
        address_line_2 (str, optional): The second line of the shipping address.
            Defaults to None.
        city (str): The city of the shipping address.
        state (str): The state of the shipping address.
        postal_code (str): The postal code of the shipping address.
        country (str): The country of the shipping address.
        created_at (datetime): The date and time the shipping address was created.

    Returns:
        str: A string representation of the shipping address.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Shipping address for Order {self.order.id}'

class ShippingMethod(models.Model):
    """
    Represents a shipping method in the database.

    Attributes:
        name (str): The name of the shipping method.
        price (float): The price of the shipping method.
        estimated_delivery_time (str): The estimated delivery time of the shipping method.
        created_at (datetime): The date and time the shipping method was created.

    Returns:
        str: A string representation of the shipping method.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_delivery_time = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
