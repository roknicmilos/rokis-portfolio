from django.test import TestCase

from apps.portfolio.tests.factories import LanguageFactory


class TestLanguage(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.language = LanguageFactory()

    def test_str(self):
        self.assertEqual(
            str(self.language),
            f'{self.language.label} ({self.language.level}/5)'
        )
