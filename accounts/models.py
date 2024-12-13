from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    """
    Represents a customer in the database.

    Attributes:
        account_id (int): The customer's account ID.
        first_name (str): The customer's first name.
        last_name (str): The customer's last name.
        email (str): The customer's email address.
        phone_number (str): The customer's phone number.
        address (str): The customer's address.
        created_at (datetime): The date and time the customer was created.
        updated_at (datetime): The date and time the customer was last updated.
        notes (str): Any additional notes about the customer.

    Returns:
        str: A string representation of the customer.
    """
    account_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"