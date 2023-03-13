from django.test import TestCase


class TestFAQViews(TestCase):
    """
    A class for testing faq views
    """
    def test_get_faq_page(self):
        """
        This test checks if the faq page is displayed
        """
        response = self.client.get('/faqs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs.html')

    def test_get_add_faq_page(self):
        """
        This test checks if the add faq page is displayed
        """
        response = self.client.get('/faqs/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_faq.html')

