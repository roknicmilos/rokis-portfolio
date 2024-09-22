from django.test import TestCase

from apps.portfolio.tests.factories import EducationFactory


class TestEducation(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.education = EducationFactory()

    def test_str(self):
        self.assertEqual(
            str(self.education),
            f"{self.education.school} - {self.education.degree}",
        )

    def test_title_property(self):
        self.assertEqual(self.education.title, str(self.education))
