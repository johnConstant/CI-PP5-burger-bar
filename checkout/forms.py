from django import forms
from .models import Order, Comment


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_type', 'order_location', 'full_name', 'email',
                  'phone_number', 'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode', 'country',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'order_type': 'Order Type',
            'order_location': 'Order Location',
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County',
            'postcode': 'Postal Code',
            'country': 'Country',
        }

        self.fields['order_type'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
