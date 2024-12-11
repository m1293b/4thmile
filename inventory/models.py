from django.db import models
from products.models import Product

# Create your models here.

class Stock(models.Model):
    """
    Represents a product's current stock level in the database.

    Attributes:
        product (Product): The product whose stock this object represents.
        quantity (int): The current number of available units of the product.
        updated_at (datetime): The date and time the stock was last updated.
        
    Returns:
        str: A string representation of the stock, including the product name.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Stock for {self.product.name}'