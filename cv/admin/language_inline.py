from django.contrib import admin

from cv.models import Language


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 0
    classes = ['collapse']
