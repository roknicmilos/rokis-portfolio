from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from cv.admin import (
    LinkInline,
    SkillInline,
    LanguageInline,
    EducationInline,
    InternshipInline,
    EmploymentInline,
    ProjectInline,
)
from cv.models import CV


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'slug',
                'title',
                'filename',
                'avatar',
                'page_count',
            ),
        }),
        (_('CONTACT (L)'), {
            'fields': (
                'email',
                'phone',
                'address_label',
                'address_link',
            ),
            'classes': ('collapse',),
        }),
        (_('HEADER (R)'), {
            'fields': (
                'first_name',
                'last_name',
                'role',
            ),
            'classes': ('collapse',),
        }),
        (_('ABOUT ME (R)'), {
            'fields': (
                'about_me',
            ),
            'classes': ('collapse',),
        }),
    )
    inlines = [
        LinkInline,
        SkillInline,
        LanguageInline,
        EmploymentInline,
        InternshipInline,
        EducationInline,
        ProjectInline,
    ]
