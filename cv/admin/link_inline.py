from django.contrib import admin

from cv.models import Link


class LinkInline(admin.TabularInline):
    model = Link
    extra = 0
