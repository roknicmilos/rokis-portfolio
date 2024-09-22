from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.portfolio.models import Education


class EducationInline(admin.StackedInline):
    model = Education
    extra = 0
    classes = ["collapse"]
    verbose_name_plural = _("EDUCATION (L)")
