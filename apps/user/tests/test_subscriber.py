from django.test import TestCase

from apps.user.tests.factories import SubscriberFactory


class TestSubscriber(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.subscriber = SubscriberFactory()

    def test_str(self):
        self.assertEqual(
            str(self.subscriber), f"Subscriber {self.subscriber.email}"
        )
