from django import forms
from .models import Menu_Item


class MenuItemForm(forms.ModelForm):
    """
    A class view creating the Menu Item form
    """
    class Meta:
        model = Menu_Item
        exclude = ['slug',]
