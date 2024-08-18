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
            'links': links,
            'skills': skills,
        }
