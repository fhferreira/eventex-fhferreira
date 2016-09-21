from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='Flavio Henrique Ferreira',
            cpf='25929881820',
            email='flaviometalvale@gmail.com',
            phone='16992084635'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Flavio Henrique Ferreira', str(self.obj))
