from django.urls import path

from cv.views import CVPDFView

app_name = 'cv'

urlpatterns = [
    path('cv/', CVPDFView.as_view(), name='index'),
]
