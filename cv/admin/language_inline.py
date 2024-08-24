from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from cv.models import Language


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 0
    classes = ['collapse']
    verbose_name_plural = _('LANGUAGES (L)')
