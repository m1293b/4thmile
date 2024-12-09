from django.test import TestCase
from home.models import Category, Product, Customer, Order, OrderItem, Payment

class CategoryTestCase(TestCase):
    def test_category_creation(self):
        """
        Tests that a Category object can be created with a given name.
        """
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

class ProductTestCase(TestCase):
    def test_product_creation(self):
        """
        Tests that a Product object can be created with a given name and category.
        """
        
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(name='Test Product', category=category)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.category, category)

class CustomerTestCase(TestCase):
    def test_customer_creation(self):
        """
        Tests that a Customer object can be created with a given first name, last name, and email.
        """
        customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
        self.assertEqual(customer.first_name, 'John')
        self.assertEqual(customer.last_name, 'Doe')
        self.assertEqual(customer.email, 'john.doe@example.com')

class OrderTestCase(TestCase):
    def test_order_creation(self):
        """
        Tests that an Order object can be created with a given customer.
        """
        
        customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
        order = Order.objects.create(customer=customer)
        self.assertEqual(order.customer, customer)

class OrderItemTestCase(TestCase):
    def test_order_item_creation(self):
        """
        Tests that an OrderItem object can be created with a given order and product.
        """
        
        customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
        order = Order.objects.create(customer=customer)
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(name='Test Product', category=category)
        order_item = OrderItem.objects.create(order=order, product=product)
        self.assertEqual(order_item.order, order)
        self.assertEqual(order_item.product, product)

class PaymentTestCase(TestCase):
    def test_payment_creation(self):
        """
        Tests that a Payment object can be created with a given order and customer.
        """
        customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
        order = Order.objects.create(customer=customer)
        payment = Payment.objects.create(order=order, customer=customer)
        self.assertEqual(payment.order, order)
        self.assertEqual(payment.customer, customer)