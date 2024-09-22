from django.test import TestCase

from apps.portfolio.tests.factories import EmploymentFactory


class TestEmployment(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.employment = EmploymentFactory()

    def test_str(self):
        self.assertEqual(
            str(self.employment),
            f"{self.employment.title} at {self.employment.company}",
        )
