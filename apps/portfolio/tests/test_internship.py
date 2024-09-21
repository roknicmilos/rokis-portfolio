from django.test import TestCase

from apps.portfolio.tests.factories import InternshipFactory


class TestInternship(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.internship = InternshipFactory()

    def test_str(self):
        self.assertEqual(
            str(self.internship),
            f'{self.internship.title} at {self.internship.company}'
        )
