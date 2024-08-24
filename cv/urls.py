from django.urls import path

from cv.views import CVPDFView

app_name = 'cv'

urlpatterns = [
    path('', CVPDFView.as_view(response_type='html'), name='index'),
    path('pdf/', CVPDFView.as_view(response_type='pdf'), name='pdf'),
    path(
        'download/',
        CVPDFView.as_view(response_type='download'),
        name='download'
    ),
]
