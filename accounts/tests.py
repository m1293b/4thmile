from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
from .models import Customer
from .views import success, profile, update_password, process_payment


class ViewTest(TestCase):

    def setUp(self):
        # Create a test user and customer for testing purposes
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="12345"
        )
        self.customer = Customer.objects.create(
            user=self.user, username="testuser", first_name="Test", last_name="User"
        )
        self.factory = RequestFactory()

    def _add_middleware_to_request(self, request):
        # Add SessionMiddleware first
        session_middleware = SessionMiddleware(get_response=lambda r: None)
        session_middleware.process_request(request)

        # Manually set the session attribute to avoid errors
        if not hasattr(request, "session"):
            setattr(request, "_session", {})

        request.session.save()

        # Then add MessageMiddleware
        message_middleware = MessageMiddleware(get_response=lambda r: None)

        from django.contrib.messages.storage.fallback import FallbackStorage

        # Manually set the messages attribute using FallbackStorage
        setattr(request, "_messages", FallbackStorage(request))

    def test_process_payment(self):
        request = self.factory.get("/process_payment/")
        request.user = self.user
        self._add_middleware_to_request(request)
        response = process_payment(request)
        self.assertEqual(response.status_code, 200)

    def test_success(self):
        request = self.factory.get("/success/")
        request.user = self.user
        self._add_middleware_to_request(request)
        response = success(request)
        self.assertEqual(response.status_code, 200)

    def test_profile_view_get(self):
        request = self.factory.get("/profile/")
        request.user = self.user
        self._add_middleware_to_request(request)
        response = profile(request)
        self.assertEqual(response.status_code, 200)

    def test_profile_view_post(self):
        data = {
            "username": "newtestuser",
            "email": "new@example.com",
            "first_name": "New",
            "last_name": "User",
            "phone_number": "1234567890",
            "address": "123 Test St",
            "notes": "Test notes",
        }
        request = self.factory.post("/profile/", data)
        request.user = self.user
        self._add_middleware_to_request(request)
        response = profile(request)
        self.assertEqual(response.status_code, 200)

    def test_update_password(self):
        data = {
            "old_password": "12345",
            "new_password1": "newpassword1",
            "new_password2": "newpassword1",
        }
        request = self.factory.post("/update_password/", data)
        request.user = self.user
        self._add_middleware_to_request(request)
        response = update_password(request)
        self.assertEqual(response.status_code, 302)
