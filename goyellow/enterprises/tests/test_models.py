from django.test import TestCase
from ..models import Enterprise


# Create your tests here.
class EnterpriseModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_enterprise = Enterprise()
        first_enterprise.enterprise_name = 'first_enterprise'
        first_enterprise.save()

        second_enterprise = Enterprise()
        second_enterprise.enterprise_name = 'second_enterprise'
        second_enterprise.save()

        saved_enterprises = Enterprise.objects.all()
        self.assertEqual(saved_enterprises.count(), 2)

        first_saved_enterprise = saved_enterprises[0]
        second_saved_enterprise = saved_enterprises[1]

        self.assertEqual(first_saved_enterprise.enterprise_name, 'first_enterprise')
        self.assertEqual(second_saved_enterprise.enterprise_name, 'second_enterprise')

    def test_enterprise_name_label(self):
        enterprise = Enterprise.objects.create(enterprise_name='enterprise_name')
        field_label = enterprise._meta.get_field('enterprise_name').verbose_name
        self.assertEquals(field_label, 'enterprise name')

    def test_enterprise_name_max_length(self):
        enterprise = Enterprise.objects.create(enterprise_name='enterprise_name')
        max_length = enterprise._meta.get_field('enterprise_name').max_length
        self.assertEquals(max_length, 100)
