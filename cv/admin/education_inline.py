from django.contrib import admin

from cv.models import Education


class EducationInline(admin.StackedInline):
    model = Education
    extra = 0
    classes = ['collapse']
