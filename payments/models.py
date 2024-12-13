from django.db import models
from orders.models import Order
from accounts.models import Customer

# Create your models here.

class Payment(models.Model):
    """
    Represents a payment in the database.

    Attributes:
        payment_id (int): A unique identifier for the payment.
        order (Order): The order that this payment belongs to.
        stripe_charge_id (str): The Stripe charge ID associated with the payment.
        customer (Customer): The customer who made the payment.
        payment_method (str): The method used to make the payment (e.g. "credit card", etc.).
        payment_date (date): The date the payment was made.
        amount (float): The amount of the payment.
        created_at (datetime): The date and time the payment was created.
        updated_at (datetime): The date and time the payment was last updated.

    Returns:
        str: A string representation of the payment.
    """
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment for Order {self.order.id} by {self.customer}"