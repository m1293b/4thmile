from django.test import TestCase
from django.urls import reverse
from .models import Order, OrderItem
from products.models import Product, Category
from django.contrib.auth.models import User

# Create your tests here.


class OrderViewsTestCase(TestCase):

    def setUp(self):
        # Set up any objects or data needed for your tests
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.order1 = Order.objects.create(user=self.user, total=10.00)
        self.category = Category.objects.create(name="Electronics")
        self.product1 = Product.objects.create(
            name="Product 1",
            price=5.00,
            stock=10,
            category=self.category,
            description="Description of Product 1",
            image="http://example.com/product1.jpg",
        )
        self.order_item1 = OrderItem.objects.create(
            order=self.order1,
            product=self.product1,
            quantity=2,
            price=self.product1.price,
        )

    def test_orders_view(self):
        # Test the Orders view
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("orders"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Order ID")
        self.assertContains(response, "Product 1")
        self.assertContains(response, "Quantity:")
