from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.utils.translation import gettext_lazy as _

from apps.portfolio.models import Project


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 0
    classes = ['collapse']
    verbose_name_plural = _('PROJECTS (R)')
    formfield_overrides = {
        models.CharField: {
            'widget': Textarea(attrs={'rows': 5, 'cols': 74})
        },
    }
