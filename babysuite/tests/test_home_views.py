from django.test import TestCase, Client
from home.models import Category, Product, Customer, Order, OrderItem, Payment
from home.views import index, product_detail, order_summary

class IndexViewTestCase(TestCase):
    def test_index_view(self):
        """
        Tests that the index view returns a 200 status code.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class ProductDetailViewTestCase(TestCase):
    def test_product_detail_view(self):
        """
        Tests that the product detail view returns a 200 status code
        when given a valid product ID.
        """
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(name='Test Product', category=category)
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)

class OrderSummaryViewTestCase(TestCase):
    def test_order_summary_view(self):
        """
        Tests that the order summary view returns a 200 status code
        when given a valid order ID.
        """
        customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
        order = Order.objects.create(customer=customer)
        response = self.client.get(f'/orders/{order.id}/summary/')
        self.assertEqual(response.status_code, 200)