from django.urls import resolve
from django.urls import reverse_lazy
from django.test import TestCase
from unittest import skip

from ..views import home_page
from ..views import details
from ..models import Enterprise


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'enterprises/home.html')


class IndexPageTest(TestCase):

    def setUp(self):
        self.name1 = 'enterprise1'
        self.name2 = 'enterprise2'
        Enterprise.objects.create(enterprise_name=self.name1)
        Enterprise.objects.create(enterprise_name=self.name2)

    def test_resolve_index_page(self):
        response = self.client.get(reverse_lazy('enterprises:index'))

        self.assertEqual(response.status_code, 200)

    def test_index_uses_correct_template(self):
        response = self.client.get(reverse_lazy('enterprises:index'))

        self.assertTemplateUsed(response, 'enterprises/enterprise_list.html')

    def test_index_displays_all_items(self):
        response = self.client.get(reverse_lazy('enterprises:index'))

        self.assertContains(response, 'enterprise1')
        self.assertContains(response, 'enterprise2')


class DetailsPageTest(TestCase):

    def setUp(self):
        self.name1 = 'enterprise1'
        self.name2 = 'enterprise2'
        Enterprise.objects.create(enterprise_name=self.name1)
        Enterprise.objects.create(enterprise_name=self.name2)

    def test_resolve_enterprises_details_page(self):
        response = self.client.get(reverse_lazy('enterprises:details', kwargs={'pk' : 1}))

        self.assertEqual(response.status_code, 200)

    def test_details_uses_correct_template(self):
        response = self.client.get(reverse_lazy('enterprises:details', kwargs={'pk': 1}))

        self.assertTemplateUsed(response, 'enterprises/enterprise_detail.html')

    def test_details_contains_enterprise_name(self):
        response1 = self.client.get(reverse_lazy('enterprises:details', kwargs={'pk': 1}))
        response2 = self.client.get(reverse_lazy('enterprises:details', kwargs={'pk': 2}))

        self.assertContains(response1, self.name1)
        self.assertContains(response2, self.name2)

    def test_details_of_missing_item_returns_404(self):
        response = self.client.get(reverse_lazy('enterprises:details', kwargs={'pk': 3}))

        self.assertEqual(response.status_code, 404)


class NewEnterprisePage(TestCase):

    def test_resolve_new_page(self):
        response = self.client.get(reverse_lazy('enterprises:new'))

        self.assertEqual(response.status_code, 200)

    def test_new_uses_correct_template_after_GET(self):
        response = self.client.get(reverse_lazy('enterprises:new'))

        self.assertTemplateUsed(response, 'enterprises/new.html')

    def test_new_redirects_to_details_after_POST(self):
        response = self.client.post(
            reverse_lazy('enterprises:new'),
            data={
                'enterprise_name': 'my_new_enterprise'
            }
        )
        self.assertEqual(response['location'], '/enterprises/1/')

    def test_new_can_save_a_POST_request(self):
        response = self.client.post(
            reverse_lazy('enterprises:new'),
            data={
                'enterprise_name':'my_new_enterprise'
            }
        )
        enterprises = Enterprise.objects.all()
        self.assertEqual(enterprises.count(), 1)

    def test_new_does_not_save_a_GET_request(self):
        response = self.client.get(
            reverse_lazy('enterprises:new')
        )
        enterprises = Enterprise.objects.all()
        self.assertEqual(enterprises.count(), 0)

    def test_new_enterprise_has_expected_name(self):
        response = self.client.post(
            reverse_lazy('enterprises:new'),
            data={
                'enterprise_name': 'my_new_enterprise'
            }
        )
        enterprise = Enterprise.objects.first()
        self.assertEqual(enterprise.enterprise_name, 'my_new_enterprise')

    def test_new_redirects_after_POST(self):
        response = self.client.post(
            reverse_lazy('enterprises:new'),
            data={
                'enterprise_name': 'my_new_enterprise'
            }
        )

        self.assertEqual(response.status_code, 302)
