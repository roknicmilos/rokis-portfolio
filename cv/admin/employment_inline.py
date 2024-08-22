from django.contrib import admin

from cv.models import Employment


class EmploymentInline(admin.StackedInline):
    model = Employment
    extra = 0
    classes = ['collapse']
