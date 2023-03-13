from django.test import TestCase


class TestProfileViews(TestCase):
    """
    A class for testing profile views
    """
    def test_get_profile_page(self):
        """
        This test checks if the profile page is displayed
        """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
