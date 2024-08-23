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
                template_name='cv/includes/educations.html',
                context={'educations': cv.ordered_educations},
            )
        )
    if cv.internships.exists():
        left_section.append(
            render_to_string(
                template_name='cv/includes/internships.html',
                context={'internships': cv.ordered_internships},
            )
        )

    return left_section


def render_right_section(cv: CV) -> list[str]:
    right_section = []
    if cv.about_me:
        right_section.append(
            render_to_string(
                template_name='cv/includes/about_me.html',
                context={'about_me': cv.about_me},
            )
        )
    if cv.employments.exists():
        right_section.append(
            render_to_string(
                template_name='cv/includes/employments.html',
                context={'employments': cv.ordered_employments},
            )
        )
    if cv.projects.exists():
        right_section.append(
            render_to_string(
                template_name='cv/includes/projects.html',
                context={'projects': cv.ordered_projects},
            )
        )

    return right_section
