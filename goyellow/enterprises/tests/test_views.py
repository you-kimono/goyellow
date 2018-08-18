from django.urls import resolve
from django.test import TestCase
from enterprises.views import home_page
from enterprises.views import details

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'enterprises/home.html')


class DetailsPageTest(TestCase):

    def test_enterprises_details_url_resolves_to_details_view(self):
        found = resolve('/enterprises/1/')
        self.assertEqual(found.func, details)

    def test_enterprises_details_url_resolves(self):
        response = self.client.get('/enterprises/1/')
        self.assertTemplateUsed(response, 'enterprises/details.html')
