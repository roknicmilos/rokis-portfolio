from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils.translation import gettext_lazy as _

from apps.portfolio.models import Portfolio
from apps.portfolio.tests.factories import (
    PortfolioFactory,
    EmploymentFactory,
    InternshipFactory,
    EducationFactory,
    SkillFactory,
    ProjectFactory,
)


class TestPortfolio(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.portfolio = PortfolioFactory()

    def test_str(self):
        self.assertEqual(str(self.portfolio), self.portfolio.title)

    def test_ordered_employments_property(self):
        fist_employment = EmploymentFactory(
            portfolio=self.portfolio,
            start='2019-01-01',
        )
        second_employment = EmploymentFactory(
            portfolio=self.portfolio,
            start='2020-01-01',
        )
        employments = self.portfolio.ordered_employments
        self.assertEqual(len(employments), 2)
        self.assertEqual(employments[0], second_employment)
        self.assertEqual(employments[1], fist_employment)

    def test_ordered_internships_property(self):
        fist_internship = InternshipFactory(
            portfolio=self.portfolio,
            start='2019-01-01',
        )
        second_internship = InternshipFactory(
            portfolio=self.portfolio,
            start='2020-01-01',
        )
        internships = self.portfolio.ordered_internships
        self.assertEqual(len(internships), 2)
        self.assertEqual(internships[0], second_internship)
        self.assertEqual(internships[1], fist_internship)

    def test_ordered_educations_property(self):
        fist_education = EducationFactory(
            portfolio=self.portfolio,
            start='2019-01-01',
        )
        second_education = EducationFactory(
            portfolio=self.portfolio,
            start='2020-01-01',
        )
        educations = self.portfolio.ordered_educations
        self.assertEqual(len(educations), 2)
        self.assertEqual(educations[0], second_education)
        self.assertEqual(educations[1], fist_education)

    def test_ordered_skills_property(self):
        fist_skill = SkillFactory(
            portfolio=self.portfolio,
            level=5,
        )
        second_skill = SkillFactory(
            portfolio=self.portfolio,
            level=1,
        )
        skills = self.portfolio.ordered_skills
        self.assertEqual(len(skills), 2)
        self.assertEqual(skills[0], fist_skill)
        self.assertEqual(skills[1], second_skill)

    def test_ordered_projects_property(self):
        fist_project = ProjectFactory(
            portfolio=self.portfolio,
            start='2019-01-01',
            end='2020-01-01',
        )
        current_project = ProjectFactory(
            portfolio=self.portfolio,
            start='2018-01-01',
            end=None,
        )
        projects = self.portfolio.ordered_projects
        self.assertEqual(len(projects), 2)
        self.assertEqual(projects[0], current_project)
        self.assertEqual(projects[1], fist_project)

    def test_left_column_segment_validation(self):
        # When left column segments are unique,
        # no validation errors should be added:
        self.portfolio.clean()
        self.assertEqual(self.portfolio.validation_errors, {})

        # When left column segments are not unique,
        # validation errors should be added:
        self.portfolio.first_left_segment = self.portfolio.second_left_segment
        with self.assertRaises(ValidationError) as context:
            self.portfolio.clean()
        expected_validation_errors = {
            'first_left_segment': [_('The segment value must be unique.')],
            'second_left_segment': [_('The segment value must be unique.')],
        }
        self.assertEqual(
            context.exception.message_dict,
            expected_validation_errors
        )

    def test_get_left_segment_order(self):
        """
        Assuming defaults are used, this should be the order
        of the left column segments:
            1. CONTACT
            2. LINKS
            3. SKILLS
            4. LANGUAGES
            5. INTERNSHIP
            6. EDUCATION
        """
        self.assertEqual(
            self.portfolio.get_left_segment_order(
                Portfolio.LeftSegment.CONTACT
            ),
            0
        )
        self.assertEqual(
            self.portfolio.get_left_segment_order(
                Portfolio.LeftSegment.LINKS
            ),
            1
        )
        self.assertEqual(
            self.portfolio.get_left_segment_order(
                Portfolio.LeftSegment.SKILLS
            ),
            2
        )
        self.assertEqual(
            self.portfolio.get_left_segment_order(
                Portfolio.LeftSegment.LANGUAGES
            ),
            3
        )
        self.assertEqual(
            self.portfolio.get_left_segment_order(
                Portfolio.LeftSegment.INTERNSHIP
            ),
            4
        )
        self.assertEqual(
            self.portfolio.get_left_segment_order(
                Portfolio.LeftSegment.EDUCATION
            ),
            5
        )

    def test_right_column_segment_validation(self):
        # When right column segments are unique,
        # no validation errors should be added:
        self.portfolio.clean()
        self.assertEqual(self.portfolio.validation_errors, {})

        # When right column segments are not unique,
        # validation errors should be added:
        self.portfolio.first_right_segment = self.portfolio.second_right_segment
        with self.assertRaises(ValidationError) as context:
            self.portfolio.clean()
        expected_validation_errors = {
            'first_right_segment': [_('The segment value must be unique.')],
            'second_right_segment': [
                _('The segment value must be unique.')],
        }
        self.assertEqual(
            context.exception.message_dict,
            expected_validation_errors
        )

    def test_get_right_segment_order(self):
        """
        Assuming defaults are used, this should be the order
        of the right column segments:
            1. ABOUT_ME
            2. EMPLOYMENT
            3. PROJECTS
        """
        self.assertEqual(
            self.portfolio.get_right_segment_order(
                Portfolio.RightSegment.ABOUT_ME
            ),
            0
        )
        self.assertEqual(
            self.portfolio.get_right_segment_order(
                Portfolio.RightSegment.EMPLOYMENT
            ),
            1
        )
        self.assertEqual(
            self.portfolio.get_right_segment_order(
                Portfolio.RightSegment.PROJECTS
            ),
            2
        )
