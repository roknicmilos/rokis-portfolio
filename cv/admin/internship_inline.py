from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from cv.models import Internship


class InternshipInline(admin.StackedInline):
    model = Internship
    extra = 0
    classes = ['collapse']
    verbose_name_plural = _('INTERNSHIP (L)')
