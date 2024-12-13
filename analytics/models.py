from django.db import models

# Create your models here.

class SalesReport(models.Model):
    """
    Represents a sales report in the database.

    Attributes:
        report_id (AutoField): The unique identifier for the report.
        date (Date): The date the report is for.
        total_sales (Decimal): The total sales for the date.
        total_orders (PositiveIntegerField): The total number of orders for the date.
        created_at (DateTime): The date and time the report was created.

    Returns:
        str: A string representation of the report.
    """
    report_id = models.AutoField(primary_key=True)
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_orders = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Sales Report for {self.date}'
