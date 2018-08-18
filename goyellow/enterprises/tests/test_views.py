from django.urls import resolve
from django.test import TestCase
from unittest import skip
from enterprises.views import home_page
from enterprises.views import details
from ..models import Enterprise

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'enterprises/home.html')


class DetailsPageTest(TestCase):

    def setUp(self):
        Enterprise.objects.create(name='enterprise1')
        Enterprise.objects.create(name='enterprise2')

    def test_resolve_enterprises_list_page(self):
        response = self.client.get('/enterprises/')
        self.assertEqual(response.status_code, 200)

    def test_enterprises_list_page_uses_correct_template(self):
        response = self.client.get('/enterprises/')
        self.assertTemplateUsed(response, 'enterprises/enterprises.html')

    def test_display_all_items(self):
        response = self.client.get('/enterprises/')

        self.assertContains(response, 'enterprise1')
        self.assertContains(response, 'enterprise2')

    def test_resolve_enterprises_details_page(self):
        response = self.client.get('/enterprises/1/')
        self.assertEqual(response.status_code, 200)

    def test_enterprises_details_url_resolves_to_details_view(self):
        found = resolve('/enterprises/1/')
        self.assertEqual(found.func, details)

    def test_enterprises_details_url_uses_correct_url(self):
        response = self.client.get('/enterprises/1/')
        self.assertTemplateUsed(response, 'enterprises/details.html')

    def test_enterprises_details_contains_enterprise_name(self):
        response1 = self.client.get('/enterprises/1/')
        response2 = self.client.get('/enterprises/2/')

        self.assertContains(response1, 'enterprise1')
        self.assertContains(response2, 'enterprise2')
