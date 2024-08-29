from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.portfolio.models import Link


class LinkInline(admin.TabularInline):
    model = Link
    extra = 0
    classes = ['collapse']
    verbose_name_plural = _('LINKS (L)')
