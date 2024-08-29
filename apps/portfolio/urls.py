from django.urls import path

from apps.portfolio.views import PortfolioPDFView

app_name = 'portfolio'

urlpatterns = [
    path('', PortfolioPDFView.as_view(response_type='html'), name='index'),
    path('pdf/', PortfolioPDFView.as_view(response_type='pdf'), name='pdf'),
    path(
        'download/',
        PortfolioPDFView.as_view(response_type='download'),
        name='download'
    ),
]
