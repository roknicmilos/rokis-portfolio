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
        (_('LEFT COLUMN | SEGMENT ORDER'), {
            'fields': (
                'first_left_segment',
                'second_left_segment',
                'third_left_segment',
                'fourth_left_segment',
                'fifth_left_segment',
                'sixth_left_segment',
            ),
            'classes': ('collapse',),
        }),
        (_('RIGHT COLUMN | SEGMENT ORDER'), {
            'fields': (
                'first_right_segment',
                'second_right_segment',
                'third_right_segment',
            ),
            'classes': ('collapse',),
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
