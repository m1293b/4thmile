from django import forms
from .models import Review


# is this correct?
class ReviewForm(forms.ModelForm):

    class Meta:

        model = Review
        fields = ["rating", "comment"]
