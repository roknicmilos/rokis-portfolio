from django.test import TestCase

from apps.portfolio.tests.factories import SkillFactory


class TestSkill(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.skill = SkillFactory()

    def test_str(self):
        self.assertEqual(
            str(self.skill),
            f'{self.skill.label} ({self.skill.level}/5)'
        )
