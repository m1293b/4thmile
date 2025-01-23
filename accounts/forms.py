from django import forms
from .models import Customer


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user details.

    Attributes:
        username (char): The user's username.
        first_name (char): The user's first name.
        last_name (char): The user's last name.
        email (email): The user's email address.
        phone_number (char): The user's phone number.
        address (text): The user's address.
        notes (text, optional): Any additional notes about the user.

    Returns:
        None
    """

    class Meta:
        model = Customer
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "address",
            "notes",
        ]
