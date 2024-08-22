from django.contrib import admin

from cv.models import Skill


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0
    classes = ['collapse']
