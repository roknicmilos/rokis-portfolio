from django.shortcuts import get_object_or_404
from django_pdf_view.pdf import PDF
from django_pdf_view.views import PDFView

from cv.models import CV


class CVPDFView(PDFView):
    cv: CV

    def create_pdf(self) -> PDF:
        self.cv = get_object_or_404(CV, slug=self.kwargs['slug'])

        pdf = PDF(
            title=self.cv.title,
            filename=self.cv.filename,
        )

        pdf.add_page(
            template_name='cv/cv.html',
            context=self._get_first_page_context(),
        )

        return pdf

    def _get_first_page_context(self):
        employments = [
            {
                'title': 'Software Engineer & Development Lead',
                'company': 'Vega IT',
                'from': 'Aug 2023',
                'until': 'Present',
                'location': 'Novi Sad, Serbia',
                'description': (
                    'In Aug 2023, I assumed the role of Development Lead, '
                    'taking on the responsibility of managing the career '
                    'progression and work satisfaction of six colleagues. '
                    'In addition the mentioned duties, I continued to work on '
                    'Python/Django and Next.js projects while also gaining '
                    'significant experience with Cypress in one of my latest '
                    'projects. I also continued mentoring colleagues and '
                    'students in Python/Django and React, while my experience '
                    'with Docker and various CI tools has further grown '
                    'during this period.'
                )
            },
            {
                'title': 'Software Engineer',
                'company': 'Vega IT',
                'from': 'Jan 2019',
                'until': 'Aug 2023',
                'location': 'Novi Sad, Serbia',
                'description': (
                    'During this period, I began my journey as a Software '
                    'Engineer, where I initially worked extensively with PHP '
                    'technologies, including Drupal, WordPress, and Symfony. '
                    'After the first one and a half years, I transitioned to '
                    'working on Python/Django and Next.js projects, a focus '
                    'that spanned over four years. In addition to my '
                    'development work, I took on leadership roles in two '
                    'internal hackathon projects and mentored colleagues and '
                    'students in Python/Django and React. I also gained '
                    'valuable experience with Docker and various CI tools. '
                    'For the last three years of this period, I exclusively '
                    'worked on Ubuntu, solidifying my proficiency with this '
                    'operating system.'
                )
            }
        ]
        links = [
            {
                'label': 'LinkedIn',
                'url': (
                    'https://www.linkedin.com/in/'
                    'milo%C5%A1-rokni%C4%87-30853bb8/'
                ),
                'type': 'linkedin',
            },
            {
                'label': 'GitHub',
                'url': 'https://github.com/roknicmilos',
                'type': 'github',
            },
        ]
        skills = [
            {'label': 'Python', 'level': 5},
            {'label': 'Django', 'level': 5},
            {'label': 'Next.js', 'level': 5},
            {'label': 'JavaScript', 'level': 5},
            {'label': 'TypeScript', 'level': 5},
            {'label': 'HTML', 'level': 5},
            {'label': 'CSS', 'level': 5},
            {'label': 'Git', 'level': 5},
            {'label': 'SQL', 'level': 4},
            {'label': 'Docker', 'level': 4},
            {'label': 'Cypress', 'level': 4},
            {'label': 'PHP', 'level': 3},
        ]
        return {
            'cv': self.cv,
            'employments': employments,
            'links': links,
            'skills': skills,
        }
