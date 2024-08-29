from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rokis_corner.views import get_index_page

urlpatterns = [
    path('', get_index_page, name='index'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', include('apps.portfolio.urls', namespace='portfolio')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
