from django.urls import path

from apps.portfolio.views import PortfolioPDFView

app_name = "portfolio"

urlpatterns = [
    path(
        "<slug:slug>/",
        PortfolioPDFView.as_view(response_type="html"),
        name="index",
    ),
    path(
        "<slug:slug>/pdf/",
        PortfolioPDFView.as_view(response_type="pdf"),
        name="pdf",
    ),
    path(
        "<slug:slug>/download/",
        PortfolioPDFView.as_view(response_type="download"),
        name="download",
    ),
]
