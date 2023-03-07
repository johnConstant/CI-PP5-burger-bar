from django import forms
from .widgets import CustomClearableFileInput
from .models import Menu_Item, Menu_Category


class MenuItemForm(forms.ModelForm):
    """
    A class view creating the Menu Item form
    """
    class Meta:
        model = Menu_Item
        exclude = ['slug',]

    featured_image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Menu_Category.objects.all()
