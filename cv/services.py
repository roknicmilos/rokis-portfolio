from cv.models import CV
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _


def get_left_column_segments(cv: CV) -> list[str]:
    """
    Returns a list of rendered HTML segments for the
    left column of the CV in the order they should be
    displayed which is configured in the CV model.
    """

    segments: list[dict] = [
        {
            'order': cv.get_left_segment_order(CV.LeftSegment.CONTACT),
            'content': render_to_string(
                template_name='cv/includes/contact.html',
                context={
                    'address_link': cv.address_link,
                    'address_label': cv.address_label,
                    'phone': cv.phone,
                    'email': cv.email,
                }
            ),
        },
    ]
    if cv.links.exists():
        segments.append({
            'order': cv.get_left_segment_order(CV.LeftSegment.LINKS),
            'content': render_to_string(
                template_name='cv/includes/links.html',
                context={'links': cv.links.all()},
            )
        })
    if cv.skills.exists():
        segments.append({
            'order': cv.get_left_segment_order(CV.LeftSegment.SKILLS),
            'content': render_to_string(
                template_name='cv/includes/skills.html',
                context={
                    'skills': cv.ordered_skills,
                    'title': _('SKILLS'),
                },
            )
        })
    if cv.languages.exists():
        segments.append({
            'order': cv.get_left_segment_order(CV.LeftSegment.LANGUAGES),
            'content': render_to_string(
                template_name='cv/includes/skills.html',
                context={
                    'skills': cv.languages.all(),
                    'title': _('LANGUAGES'),
                },
            )
        })
    if cv.internships.exists():
        segments.append({
            'order': cv.get_left_segment_order(CV.LeftSegment.INTERNSHIP),
            'content': render_to_string(
                template_name='cv/includes/internship.html',
                context={'internships': cv.ordered_internships},
            )
        })
    if cv.educations.exists():
        segments.append({
            'order': cv.get_left_segment_order(CV.LeftSegment.EDUCATION),
            'content': render_to_string(
                template_name='cv/includes/education.html',
                context={'educations': cv.ordered_educations},
            )
        })

    return [
        segment['content'] for segment
        in sorted(segments, key=lambda x: x['order'])
    ]


def render_right_column_segments(cv: CV) -> list[str]:
    segments: list[dict] = []
    if cv.about_me:
        segments.append({
            'order': cv.get_right_segment_order(CV.RightSegment.ABOUT_ME),
            'content': render_to_string(
                template_name='cv/includes/about_me.html',
                context={'about_me': cv.about_me},
            )
        })
    if cv.employments.exists():
        segments.append({
            'order': cv.get_right_segment_order(CV.RightSegment.EMPLOYMENT),
            'content': render_to_string(
                template_name='cv/includes/employment.html',
                context={'employments': cv.ordered_employments},
            )
        })
    if cv.projects.exists():
        segments.append({
            'order': cv.get_right_segment_order(CV.RightSegment.PROJECTS),
            'content': render_to_string(
                template_name='cv/includes/projects.html',
                context={'projects': cv.ordered_projects},
            )
        })

    return [
        segment['content'] for segment
        in sorted(segments, key=lambda x: x['order'])
    ]
