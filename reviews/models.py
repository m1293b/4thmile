from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Review(models.Model):
    """
    Represents a review of a product in the database.

    Attributes:
        review_id (int): A unique identifier for the review object.
        product (Product): The product being reviewed.
        user (User): The user who wrote the review.
        rating (int): The rating given by the user.
        comment (str): The comment written by the user.
        created_at (datetime): The date and time the review was created.

    Returns:
        str: A string representation of the review, including the product name,
        the user's username, the rating given, and the comment written.
    """

    review_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Product"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    rating = models.PositiveIntegerField(
        verbose_name="Rating",
        choices=[
            (1, "1 Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ],
    ) 
    comment = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.product.name}"
