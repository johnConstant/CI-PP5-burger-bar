from django import forms
from .models import FAQ


class FaqForm(forms.ModelForm):
    """
    A class view creating the FAQ form
    """
    class Meta:
        model = FAQ
        fields = "__all__"
