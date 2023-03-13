from django.test import TestCase


class TestCartViews(TestCase):
    """
    A class for testing cart views
    """
    def test_get_cart_page(self):
        """
        This test checks if the cart page is displayed
        """
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
