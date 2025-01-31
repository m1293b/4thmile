from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    """
    Represents a product category in the database.

    Attributes:
        category_id (int): A unique identifier for the category.
        name (str): The category's name.
        main_category (str): Main category of product.
        description (str): The category's description.
        created_at (datetime): The date and time the category was created.
        updated_at (datetime): The date and time the category was last updated.

    Returns:
        str: A string representation of the category.
    """
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, blank=True)
    main_category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Ensure tag names are unique

    def __str__(self):
        return self.name


class Product(models.Model):
    """
        Represents a product in the database.

        Attributes:
            name (str): The name of the product.
            description (str): A brief description of the product.
            price (float): The regular price of the product.
            stock (int): The number of units available for sale.
            category (Category): The category to which this product belongs.
            color (str): The color of the product, if applicable.
            size (str): The size of the product, if applicable.
            tags (ManyToManyField[Tag]): Tags associated with the product for categorization and search.
            created_at (datetime): Timestamp indicating when the product was first added to the database.
            updated_at (datetime): Timestamp indicating when the product was last updated in the database.
            notes (str): Additional information or notes regarding the product.
            smiles (int): The count of positive feedback received from customers for this product.
            purchases (int): The total number of times this product has been purchased by customers.
            views (int): The count of views this product received in the last 24 hours, indicating interest level.
            sales (int): The total number of sales recorded for this product.
            is_on_sale (bool): A boolean flag indicating if the product is currently being offered at a discounted price.
            sale_price (float): If `is_on_sale` is true, this attribute represents the discounted sale price.
        Returns:
            str: A string representation of the product, typically displaying its name and possibly other attributes for easy identification in lists or queries.
    """

    name = models.CharField(max_length=100, default="New product")
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    color = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=10, blank=True)
    tags = models.ManyToManyField(Tag, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    smiles = models.IntegerField(default=0)
    purchases = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    sales = models.IntegerField(default=0)
    is_on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=999)

    def __str__(self):
        return self.name
