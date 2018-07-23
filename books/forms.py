from django import forms
from .models import BookReview


class ReviewForm(forms.ModelForm):

    class Meta:
        model = BookReview
        exclude = ["user", "book", "created_date", "modified_date"]
