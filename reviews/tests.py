from django.test import TestCase, Client


class AddReviewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Setup necessary objects like user, product here.

    def test_add_review_success(self):
        response = self.client.post(
            "/reviews/add/1/", {"rating": 5, "comment": "Great product!"}
        )
        self.assertContains(response, "Review added successfully!")
