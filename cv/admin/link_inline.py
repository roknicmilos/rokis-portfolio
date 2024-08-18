from django.contrib import admin

from cv.models import Link


class LinkInline(admin.StackedInline):
    model = Link
    extra = 0
