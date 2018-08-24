from django.test import TestCase
from ..models import Enterprise


# Create your tests here.
class EnterpriseModelTest(TestCase):

    enterprise_name = "my_test_enterprise"
    enterprise_address = "Viale Fratelli Cervi, 6"

    def test_saving_and_retrieving_items(self):
        first_enterprise = Enterprise()
        first_enterprise.enterprise_name = 'first_enterprise'
        first_enterprise.save()

        second_enterprise = Enterprise()
        second_enterprise.enterprise_name = 'second_enterprise'
        second_enterprise.save()

        saved_enterprises = Enterprise.objects.all()
        self.assertEqual(saved_enterprises.count(), 2)
        self.assertEqual(saved_enterprises[0].enterprise_name, 'first_enterprise')
        self.assertEqual(saved_enterprises[1].enterprise_name, 'second_enterprise')

    def test_saved_and_retrieved_enterprise_has_expected_name(self):
        enterprise = Enterprise()
        enterprise.enterprise_name = self.enterprise_name
        enterprise.save()
        saved_enterprise = Enterprise.objects.first()
        self.assertEqual(saved_enterprise.enterprise_name, self.enterprise_name)

    def test_enterprise_name_label(self):
        enterprise = Enterprise.objects.create(enterprise_name=self.enterprise_name)
        field_label = enterprise._meta.get_field('enterprise_name').verbose_name
        self.assertEquals(field_label, 'enterprise name')

    def test_enterprise_name_max_length(self):
        enterprise = Enterprise.objects.create(enterprise_name=self.enterprise_name)
        max_length = enterprise._meta.get_field('enterprise_name').max_length
        self.assertEquals(max_length, 100)

    def test_saved_and_retrieved_enterprise_has_expected_address(self):
        enterprise = Enterprise()
        enterprise.enterprise_address = self.enterprise_address
        enterprise.save()

        saved_enterprise = Enterprise.objects.first()
        self.assertEqual(saved_enterprise.enterprise_address, self.enterprise_address)

    def test_enterprise_address_label(self):
        enterprise = Enterprise.objects.create(
            enterprise_name=self.enterprise_name,
            enterprise_address=self.enterprise_address
        )
        field_label = enterprise._meta.get_field('enterprise_address').verbose_name
        self.assertEquals(field_label, 'enterprise address')
