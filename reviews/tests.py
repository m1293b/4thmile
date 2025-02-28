from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product, Category
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.models import User


class ReviewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Test Product",
            description="A product for testing",
            price=19.99,
            stock=10,
            category=self.category,
        )

    def test_add_review_unauthenticated(self):
        form_data = {
            "title": "Great product",
            "content": "I really liked it!",
            "rating": 5,
        }
        response = self.client.post(
            reverse("add_review", args=[self.product.pk]), data=form_data
        )
        self.assertEqual(response.status_code, 302)  # Redirects to login page

    def test_add_review_authenticated(self):
        self.client.login(username="testuser", password="12345")
        form_data = {
            "title": "Great product",
            "content": "I really liked it!",
            "rating": 5,
        }
        response = self.client.post(
            reverse("add_review", args=[self.product.pk]), data=form_data
        )
        self.assertEqual(
            response.status_code, 200
        )  # Redirects after successful form submission

    def test_add_review_form_invalid(self):
        self.client.login(username="testuser", password="12345")
        form_data = {
            "title": "",
            "content": "I really liked it!",
            "rating": 11,  # Invalid rating
        }
        response = self.client.post(
            reverse("add_review", args=[self.product.pk]), data=form_data
        )
        self.assertEqual(response.status_code, 200)  # Should display form errors
        
    def test_remove_review(self):
        self.client.login(username="testuser", password="12345")
        review = Review.objects.create(
            product=self.product,
            user=self.user,
            title="Great product",
            content="I really liked it!",
            rating=5,
        )
        response = self.client.post(reverse("remove_review", args=[review.pk]))
        self.assertEqual(response.status_code, 302)  # Redirects after successful removal
        self.assertFalse(Review.objects.filter(pk=review.pk).exists())  # Review should be deleted
