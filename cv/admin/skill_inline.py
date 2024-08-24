from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from cv.models import Skill


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0
    classes = ['collapse']
    verbose_name_plural = _('SKILLS (R)')
