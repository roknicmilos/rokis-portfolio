from django.test import TestCase

from apps.portfolio.tests.factories import LinkFactory


class TestLink(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.link = LinkFactory()

    def test_str(self):
        self.assertEqual(
            str(self.link),
            f'{self.link.label} ({self.link.get_type_display()})'
        )
