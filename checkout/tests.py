from django.test import TestCase
from django.http import HttpRequest
from .forms import OrderForm, CommentForm


class TestCheckoutViews(TestCase):
    """
    A class for testing checkout views
    """
    def test_get_checkout_page(self):
        """
        This test checks if the checkout page is displayed
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')
