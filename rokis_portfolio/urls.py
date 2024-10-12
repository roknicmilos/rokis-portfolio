from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rokis_portfolio.views import IndexView

# TODO: separate MAIN site from portfolio site
#   > main site as a different project (different web framework?)
#      - for now, it can be just HTML/CSS/JS
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("health/", include("health_check.urls")),
    path("account/", include("apps.user.urls", namespace="user")),
    path("<slug:slug>/", include("apps.portfolio.urls", namespace="portfolio")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
