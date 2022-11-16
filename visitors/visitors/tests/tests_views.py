from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomepageTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse('Home_visitors'))
        self.assertEqual(response.status_code, 200)
    
    def test_template(self):
        response = self.client.get(reverse('Home_visitors'))
        self.assertTemplateUsed(response, "Home_visitors.html")