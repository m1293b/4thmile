from django.db import models

class Customer(models.Model):
    """
    Represents a customer in the database.

    Attributes:
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

class Product(models.Model):
    """
    Represents a product in the database.

    Attributes:
        name (str): The product's name.
        description (str): The product's description.
        price (float): The product's price.
        image_url (str): The URL of the product's image.
        created_at (datetime): The date and time the product was created.
        updated_at (datetime): The date and time the product was last updated.
        notes (str): Any additional notes about the product.
        smiles (int): The number of customers who have left a positive feedback (smile) for the product.
        purchases (int): The number of times the product has been purchased.
        views (int): The number of customers who have viewed the product in the last 24 hours.

    Returns:
        str: A string representation of the product.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    smiles = models.IntegerField(default=0)
    purchases = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    """
    Represents an order in the database.

    Attributes:
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
        order (Order): The order that this item belongs to.
        product (Product): The product that this item represents.
        quantity (int): The quantity of the product ordered.
        created_at (datetime): The date and time the order item was created.
        updated_at (datetime): The date and time the order item was last updated.

    Returns:
        str: A string representation of the order item.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"

class Payment(models.Model):
    """
    Represents a payment in the database.

    Attributes:
        order (Order): The order that this payment belongs to.
        customer (Customer): The customer who made the payment.
        payment_method (str): The method used to make the payment (e.g. "credit card", etc.).
        payment_date (date): The date the payment was made.
        amount (float): The amount of the payment.
        created_at (datetime): The date and time the payment was created.
        updated_at (datetime): The date and time the payment was last updated.

    Returns:
        str: A string representation of the payment.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment for Order {self.order.id} by {self.customer}"