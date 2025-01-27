from django.test import TestCase
from django.urls import reverse
from .models import Product, Category
from reviews.models import Review
from django.contrib.auth.models import User

# Create your tests here.


class ProductsViewTest(TestCase):
    def setUp(self):
        # Create categories and products for testing
        self.category1 = Category.objects.create(
            name="Category 1", friendly_name="category-1", main_category="Clothes"
        )
        self.category2 = Category.objects.create(
            name="Category 2", friendly_name="category-2"
        )

        Product.objects.create(
            name="Product A",
            category=self.category1,
            stock=10,
            price=19.99,
            description="Description A",
        )
        Product.objects.create(
            name="Product B",
            category=self.category1,
            stock=0,
            price=19.99,
            description="Description B",
        )
        Product.objects.create(
            name="Searchable Product",
            category=self.category2,
            stock=5,
            price=19.99,
            description="Description C",
        )

    def test_view_products_no_query(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Product A")
        self.assertContains(response, "Product B")  # Out of stock

    def test_search_query(self):
        response = self.client.get(reverse("products"), {"q": "searchable"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Searchable Product")

    def test_filter_by_main_category(self):
        response = self.client.get(
            reverse("products"), {"main_category": self.category1.main_category}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Product A")
        self.assertNotContains(response, "Searchable Product")  # Different category

    def test_filter_by_subcategory(self):
        response = self.client.get(reverse("products"), {"category": "category-1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Product A")
        self.assertNotContains(response, "Searchable Product")  # Different category

    def test_sorting_products(self):
        response = self.client.get(reverse("products"), {"sort": "-name"})
        self.assertEqual(response.status_code, 200)
        products_list = [p.name for p in Product.objects.all().order_by("-name")]
        page_content = response.content.decode("utf-8")
        for product_name in products_list:
            self.assertIn(product_name, page_content)


class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(
            name="Category 1", friendly_name="category-1", main_category="Clothes"
        )
        self.user = User.objects.create_user(username="testuser", password="password")
        # Create a product and reviews for testing
        self.product = Product.objects.create(
            name="Detailed Product",
            stock=10,
            price=19.99,
            category=self.category1,
            description="A detailed description.",
        )
        Review.objects.create(
            product=self.product,
            comment="Great product!",
            created_at="2023-01-01",
            rating=5,
            user=self.user,
        )
        Review.objects.create(
            product=self.product,
            comment="Not bad.",
            created_at="2023-02-01",
            rating=2,
            user=self.user,
        )

    def test_product_detail_view(self):
        response = self.client.get(reverse("product_detail", args=[self.product.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Detailed Product")
        self.assertContains(response, "Great product!")
        self.assertContains(response, "Not bad.")

    def test_product_not_found(self):
        response = self.client.get(reverse("product_detail", args=[999]))
        self.assertEqual(response.status_code, 404)
