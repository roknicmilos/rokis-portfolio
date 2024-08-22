from django.contrib import admin
from django.db import models
from django.forms import Textarea

from cv.models import Project


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 0
    classes = ['collapse']
    formfield_overrides = {
        models.CharField: {
            'widget': Textarea(attrs={'rows': 5, 'cols': 74})
        },
    }
