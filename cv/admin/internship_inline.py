from django.contrib import admin

from cv.models import Internship


class InternshipInline(admin.StackedInline):
    model = Internship
    extra = 0
    classes = ['collapse']
