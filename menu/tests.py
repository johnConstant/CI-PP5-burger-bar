from django.test import TestCase


class TestMenuViews(TestCase):
    """
    A class for testing menu views
    """
    def test_get_menu_page(self):
        """
        This test checks if the articles page is displayed
        """
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
