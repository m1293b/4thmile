from django import forms
from django.contrib.auth.forms import PasswordChangeForm
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


class CustomPasswordChangeForm(PasswordChangeForm):
    """
    A custom form for changing a user's password.

    This form extends the default Django PasswordChangeForm to customize
    the behavior or presentation of the password change process if needed.

    Attributes:
        old_password (char): The user's current password.
        new_password1 (char): The user's new password.
        new_password2 (char): The user's new password confirmation.

    """

    old_password = forms.CharField(
        label="Current password",
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
        help_text="Enter your current password to confirm it.",
    )

    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=(
            "New passwords must be at least 8 characters, and include a number, an uppercase letter, "
            "a lowercase letter, and a special character (e.g., !@#$%^&*)."
        ),
    )

    new_password2 = forms.CharField(
        label="New password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Enter the same password as above, for verification purposes.",
    )
