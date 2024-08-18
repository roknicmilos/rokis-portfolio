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

    def _get_first_page_context(self) -> dict:
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
            'avatar_url': self._get_absolut_avatar_url(),
            'skills': skills,
        }

    def _get_absolut_avatar_url(self) -> str:
        if self.cv.avatar:
            return self.request.build_absolute_uri(self.cv.avatar.url)
        return ''
