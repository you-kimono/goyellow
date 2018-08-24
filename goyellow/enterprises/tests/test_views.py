from django.urls import resolve
from django.urls import reverse_lazy
from django.test import TestCase

from ..views import home_page
from ..models import Enterprise


# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'enterprises/home.html')


class EnterpriseListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_enterprises = 14
        for enterprise_id in range(number_of_enterprises):
            Enterprise.objects.create(enterprise_name='enterprise' + str(enterprise_id))

    def test_resolve_enterprise_list_page(self):
        response = self.client.get(reverse_lazy('enterprises:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy('enterprises:index'))
        self.assertEqual(response.status_code, 200)

    def test_enterprise_list_uses_correct_template(self):
        response = self.client.get(reverse_lazy('enterprises:index'))
        self.assertTemplateUsed(response, 'enterprises/enterprise_list.html')

    def test_enterprise_list_displays_all_items(self):
        response = self.client.get(reverse_lazy('enterprises:index'))

        self.assertContains(response, 'enterprise13')
        self.assertContains(response, 'enterprise12')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse_lazy('enterprises:index'))
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['enterprise_list']), 10)

    def test_lists_all_enterprises(self):
        response = self.client.get(reverse_lazy('enterprises:index')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['enterprise_list']), 4)


class DetailsPageTest(TestCase):

    def setUp(self):
        self.name1 = 'enterprise1'
        self.name2 = 'enterprise2'
        self.address1 = 'enterprise_address1'
        self.address2 = 'enterprise_address2'
        Enterprise.objects.create(
            enterprise_name=self.name1,
            enterprise_address=self.address1
        )
        Enterprise.objects.create(
            enterprise_name=self.name2,
            enterprise_address=self.address2
        )

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
                'enterprise_name': 'my_new_enterprise',
                'enterprise_address': 'my_new_address'
            }
        )
        self.assertEqual(response['location'], '/enterprises/1/')

    def test_new_can_save_a_POST_request(self):
        self.client.post(
            reverse_lazy('enterprises:new'),
            data={
                'enterprise_name': 'my_new_enterprise',
                'enterprise_address': 'my_new_address'
            }
        )
        enterprises = Enterprise.objects.all()
        self.assertEqual(enterprises.count(), 1)

    def test_new_does_not_save_a_GET_request(self):
        self.client.get(
            reverse_lazy('enterprises:new')
        )
        enterprises = Enterprise.objects.all()
        self.assertEqual(enterprises.count(), 0)

    def test_new_enterprise_has_expected_name(self):
        response = self.client.post(
            reverse_lazy('enterprises:new'),
            data={
                'enterprise_name': 'my_new_enterprise',
                'enterprise_address': 'my_new_address'
            }
        )
        enterprise = Enterprise.objects.first()
        self.assertEqual(enterprise.enterprise_name, 'my_new_enterprise')

    def test_new_enterprise_has_expected_address(self):
        self.client.post(
            reverse_lazy('enterprises:new'),
            data={
                'enterprise_name': 'my_new_enterprise',
                'enterprise_address': 'my_new_address'
            }
        )
        enterprise = Enterprise.objects.first()
        self.assertEqual(enterprise.enterprise_address, 'my_new_address')

    def test_new_redirects_after_POST(self):
        response = self.client.post(
            reverse_lazy('enterprises:new'),
            data={
                'enterprise_name': 'my_new_enterprise',
                'enterprise_address': 'my_new_address'
            }
        )

        self.assertEqual(response.status_code, 302)
