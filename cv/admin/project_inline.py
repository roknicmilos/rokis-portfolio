from django.contrib import admin

from cv.models import Project


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 0
    classes = ['collapse']
