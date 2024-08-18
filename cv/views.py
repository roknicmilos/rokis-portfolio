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
        return {
            'cv': self.cv,
            'avatar_url': self._get_absolut_avatar_url(),
        }

    def _get_absolut_avatar_url(self) -> str:
        if self.cv.avatar:
            return self.request.build_absolute_uri(self.cv.avatar.url)
        return ''
