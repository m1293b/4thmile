from django.db import models

# Create your models here.

class Category(models.Model):
    
    class Meta:
        verbose_name_plural = 'Categories'
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
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    main_category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Represents a product in the database.

    Attributes:
        product_id (int): A unique identifier for the product.
        name (str): The product's name.
        description (str): The product's description.
        price (float): The product's price.
        stock (int): The number of available units of the product.
        category (Category): The category to which the product belongs.
        created_at (datetime): The date and time the product was created.
        updated_at (datetime): The date and time the product was last updated.
        notes (str): Any additional notes about the product.
        smiles (int): The number of customers who have left a positive feedback (smile) for the product.
        purchases (int): The number of times the product has been purchased.
        views (int): The number of customers who have viewed the product in the last 24 hours.
        sales (int): The number of times the product has been sold.
        is_on_sale (bool): Indicates whether the product is currently on sale.
        sale_price (float): The price of the product during a sale.

    Returns:
        str: A string representation of the product.
    """
    product_id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100, default=999)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
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

class ProductImage(models.Model):
    
    """
    Represents a product image in the database.

    Attributes:
        product_image_id (int): A unique identifier for the product image.
        product (Product): The product to which this image belongs.
        image (ImageField): The image file.
        alt_text (str): The alt text for the image.
        created_at (datetime): The date and time the image was created.

    Returns:
        str: A string representation of the product image.
    """
    product_image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/product_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return super().__str__()
