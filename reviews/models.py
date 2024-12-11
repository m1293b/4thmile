from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Review(models.Model):
    """
    Represents a review of a product in the database.

    Attributes:
        product (Product): The product being reviewed.
        user (User): The user who wrote the review.
        rating (int): The rating given by the user.
        comment (str): The comment written by the user.
        created_at (datetime): The date and time the review was created.

    Returns:
        str: A string representation of the review, including the product name,
        the user's username, the rating given, and the comment written.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Review by {self.user.username} on {self.product.name}'
