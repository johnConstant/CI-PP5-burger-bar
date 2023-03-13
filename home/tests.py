from django.test import TestCase


class TestHomeViews(TestCase):
    """
    A class for testing profile views
    """
    def test_get_index_page(self):
        """
        This test checks if the home page is displayed
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about_page(self):
        """
        This test checks if the about page is displayed
        """
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about_us.html')

    def test_get_privacy_page(self):
        """
        This test checks if the privacy policy page is displayed
        """
        response = self.client.get('/privacy-policy')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacy_policy.html')
