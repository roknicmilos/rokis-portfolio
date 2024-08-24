from cv.models import CV
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _


def render_left_column_segments(cv: CV) -> list[str]:
    segments = []
    if cv.links.exists():
        segments.append(
            render_to_string(
                template_name='cv/includes/links.html',
                context={'links': cv.links.all()},
            )
        )
    if cv.skills.exists():
        segments.append(
            render_to_string(
                template_name='cv/includes/skills.html',
                context={
                    'skills': cv.ordered_skills,
                    'title': _('SKILLS'),
                },
            )
        )
    if cv.languages.exists():
        segments.append(
            render_to_string(
                template_name='cv/includes/skills.html',
                context={
                    'skills': cv.languages.all(),
                    'title': _('LANGUAGES'),
                },
            )
        )
    if cv.educations.exists():
        segments.append(
            render_to_string(
                template_name='cv/includes/educations.html',
                context={'educations': cv.ordered_educations},
            )
        )
    if cv.internships.exists():
        segments.append(
            render_to_string(
                template_name='cv/includes/internships.html',
                context={'internships': cv.ordered_internships},
            )
        )

    return segments


def render_right_column_segments(cv: CV) -> list[str]:
    segments = []
    if cv.about_me:
        segments.append(
            render_to_string(
                template_name='cv/includes/about_me.html',
                context={'about_me': cv.about_me},
            )
        )
    if cv.employments.exists():
        segments.append(
            render_to_string(
                template_name='cv/includes/employments.html',
                context={'employments': cv.ordered_employments},
            )
        )
    if cv.projects.exists():
        segments.append(
            render_to_string(
                template_name='cv/includes/projects.html',
                context={'projects': cv.ordered_projects},
            )
        )

    return segments
