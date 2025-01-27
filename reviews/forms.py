from django import forms
from .models import Review


# is this correct?
class ReviewForm(forms.ModelForm):
    """
    This module contains forms for handling user reviews and ratings.

    Forms:
    - ReviewForm: Allows users to submit reviews for products or services.
    - RatingForm: Captures ratings given by users.

    Each form ensures proper validation of input data before submission.
    """

    class Meta:

        model = Review
        fields = ["rating", "comment"]
