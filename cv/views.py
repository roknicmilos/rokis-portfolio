from django.shortcuts import get_object_or_404
from django_pdf_view.pdf import PDF
from django_pdf_view.views import PDFView

from cv.models import CV


class CVPDFView(PDFView):
    template_name = 'cv/cv.html'
    css_paths = [
        'cv/css/'
    ]
    cv: CV

    def create_pdf(self) -> PDF:
        self.cv = get_object_or_404(CV, slug=self.kwargs['slug'])
        return PDF(
            template_name=self.template_name,
            title=self.cv.title,
            filename=self.cv.filename,
            context=self.get_context(),
            css_paths=self.css_paths.copy(),
        )

    def get_context(self) -> dict:
        context = super().get_context()
        context['cv'] = self.cv
        context['avatar_url'] = self._get_absolut_avatar_url()
        return context

    def _get_absolut_avatar_url(self) -> str:
        if self.cv.avatar:
            return self.request.build_absolute_uri(self.cv.avatar.url)
        return ''
