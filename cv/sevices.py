from cv.models import CV
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _


def render_left_section(cv: CV) -> list[str]:
    left_section = []
    if cv.links.exists():
        left_section.append(
            render_to_string(
                template_name='cv/includes/links.html',
                context={'links': cv.links.all()},
            )
        )
    if cv.skills.exists():
        left_section.append(
            render_to_string(
                template_name='cv/includes/skills.html',
                context={
                    'skills': cv.ordered_skills,
                    'title': _('SKILLS'),
                },
            )
        )
    if cv.languages.exists():
        left_section.append(
            render_to_string(
                template_name='cv/includes/skills.html',
                context={
                    'skills': cv.languages.all(),
                    'title': _('LANGUAGES'),
                },
            )
        )
    if cv.educations.exists():
        left_section.append(
            render_to_string(
                template_name='cv/includes/education.html',
                context={'educations': cv.ordered_educations},
            )
        )

    return left_section
