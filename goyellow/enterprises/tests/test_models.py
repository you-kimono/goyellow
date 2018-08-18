from django.test import TestCase
from ..models import Enterprise


# Create your tests here.
class EnterpriseModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_enterprise = Enterprise()
        first_enterprise.name = 'first_enterprise'
        first_enterprise.save()

        second_enterprise = Enterprise()
        second_enterprise.name = 'second_enterprise'
        second_enterprise.save()

        saved_enterprises = Enterprise.objects.all()
        self.assertEqual(saved_enterprises.count(), 2)

        first_saved_enterprise = saved_enterprises[0]
        second_saved_enterprise = saved_enterprises[1]

        self.assertEqual(first_saved_enterprise.name, 'first_enterprise')
        self.assertEqual(second_saved_enterprise.name, 'second_enterprise')
