from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from django.test import Client
from accounts.models import Customer


# Create your tests here.


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.cart = Cart.objects.create(user=self.user)
        self.customer = Customer.objects.create(user=self.user, username="Test User")

        self.product1 = {"name": "Product 1", "price": 10.0}
        self.product2 = {"name": "Product 2", "price": 20.0}

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Baby Suite")

    def test_about_view(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Us")

    def test_contact_view(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "How to contact us")
