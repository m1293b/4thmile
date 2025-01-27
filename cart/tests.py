from django.test import TestCase, Client  # Import Client here
from django.urls import reverse  # Import reverse here
import json
from django.contrib.auth.models import User
from products.models import Product, Category  # Import Category model


class CartTestCase(TestCase):
    def setUp(self):
        # Create a category for testing
        self.category = Category.objects.create(name="Test Category")

        # Create test user and login
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

        # Create a product with a valid category_id
        self.product = Product.objects.create(
            name="Test Product",
            price=10.00,
            stock=20,
            category=self.category,  # Associate the product with the created category
        )

    def test_cart_summary(self):
        response = self.client.get(reverse("cart_summary"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("cart_products", response.context)

    def test_add_to_cart(self):
        # Ensure a clean state (clear the cart if necessary)
        self.client.session.clear()

        response = self.client.post(
            reverse("add_to_cart"), {"product_id": str(self.product.pk), "quantity": 1}
        )

        data = json.loads(response.content)
        self.assertEqual(data["message"], "1x Test Product added to cart.")
        self.assertEqual(data["cart_len"], 1)  # Expected value

    def test_update_cart(self):
        # First, add the product to the cart
        self.client.post(
            reverse("add_to_cart"), {"product_id": str(self.product.pk), "quantity": 3}
        )

        response = self.client.post(
            reverse("update_cart"), {"product_id": str(self.product.pk), "quantity": 5}
        )
        data = json.loads(response.content)
        self.assertEqual(data["message"], "Quantity updated to 5 for Test Product.")
        self.assertEqual(data["cart_len"], 5)

    def test_remove_from_cart(self):
        # First, ensure the product is added to the cart
        response = self.client.post(
            reverse("add_to_cart"), {"product_id": str(self.product.pk), "quantity": 1}
        )

        # Now attempt to remove the product from the cart
        response = self.client.post(
            reverse("remove_from_cart"),
            {"product_id": str(self.product.pk), "quantity": 1},
        )

        data = json.loads(response.content)
        self.assertEqual(data["message"], f"1x {self.product.name} removed from cart.")
        self.assertEqual(data["cart_len"], 0)

    def test_clear_all_carts_authenticated(self):
        # First, add the product to the cart
        self.client.post(
            reverse("add_to_cart"), {"product_id": str(self.product.pk), "quantity": 2}
        )
        response = self.client.get(reverse("clear_all_carts"))
        data = json.loads(response.content)
        self.assertEqual(
            data["message"],
            "All carts, cart items, and the session cart have been cleared successfully.",
        )

    def test_checkout_authenticated(self):
        # First, add the product to the cart
        self.client.post(
            reverse("add_to_cart"), {"product_id": str(self.product.pk), "quantity": 2}
        )

        response = self.client.get(reverse("checkout"))
        self.assertEqual(response.status_code, 200)