from django.test import TestCase

from apps.portfolio.tests.factories import ProjectFactory


class TestProject(TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.project = ProjectFactory()

    def test_str(self):
        self.assertEqual(
            str(self.project), f"{self.project.name} - {self.project.role}"
        )
