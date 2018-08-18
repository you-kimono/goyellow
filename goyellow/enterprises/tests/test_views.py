from django.urls import resolve
from django.urls import reverse_lazy
from django.test import TestCase
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
        self.name1 = 'enterprise1'
        self.name2 = 'enterprise2'
        Enterprise.objects.create(name=self.name1)
        Enterprise.objects.create(name=self.name2)

    def test_resolve_index_page(self):
        response = self.client.get(reverse_lazy('enterprises:index'))

        self.assertEqual(response.status_code, 200)

    def test_index_uses_correct_template(self):
        response = self.client.get(reverse_lazy('enterprises:index'))

        self.assertTemplateUsed(response, 'enterprises/enterprises.html')

    def test_display_all_items(self):
        response = self.client.get(reverse_lazy('enterprises:index'))

        self.assertContains(response, 'enterprise1')
        self.assertContains(response, 'enterprise2')

    def test_resolve_enterprises_details_page(self):
        response = self.client.get(reverse_lazy('enterprises:details', kwargs={'pk' : 1}))

        self.assertEqual(response.status_code, 200)

    def test_enterprises_details_url_resolves_to_details_view(self):
        found = resolve(reverse_lazy('enterprises:details', kwargs={'pk': 1}))

        self.assertEqual(found.func, details)

    def test_enterprises_details_url_uses_correct_url(self):
        response = self.client.get(reverse_lazy('enterprises:details', kwargs={'pk': 1}))

        self.assertTemplateUsed(response, 'enterprises/details.html')

    def test_enterprises_details_contains_enterprise_name(self):
        response1 = self.client.get(reverse_lazy('enterprises:details', kwargs={'pk': 1}))
        response2 = self.client.get(reverse_lazy('enterprises:details', kwargs={'pk': 2}))

        self.assertContains(response1, self.name1)
        self.assertContains(response2, self.name2)
