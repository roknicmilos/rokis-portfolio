from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from apps.portfolio.admin import (
    LinkInline,
    SkillInline,
    LanguageInline,
    EducationInline,
    InternshipInline,
    EmploymentInline,
    ProjectInline,
)
from apps.portfolio.models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'portfolio_link',
        'is_published',
        'created',
        'modified',
    )
    fieldsets = (
        (None, {
            'fields': (
                'is_published',
                'portfolio_link',
                'id',
                'created',
                'modified',
                'slug',
                'title',
                'filename',
                'page_count',
            ),
        }),
        (_('Left Column | Segment Order'), {
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
        (_('Right Column | Segment Order'), {
            'fields': (
                'first_right_segment',
                'second_right_segment',
                'third_right_segment',
            ),
            'classes': ('collapse',),
        }),
        (_('*IMAGE (L)'), {
            'fields': (
                'avatar',
            ),
            'classes': ('collapse',),
        }),
        (_('*CONTACT (L)'), {
            'fields': (
                'email',
                'phone',
                'address_label',
                'address_link',
            ),
            'classes': ('collapse',),
        }),
        (_('*HEADER (R)'), {
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
    readonly_fields = (
        'id',
        'created',
        'modified',
        'portfolio_link',
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

    @admin.display(description=_('Portfolio Link'))
    def portfolio_link(self, obj: Portfolio = None) -> str:
        if not obj.pk:
            return _('Save the Portfolio first to generate the link.')

        href = reverse(viewname='portfolio:index', kwargs={'slug': obj.slug})
        label = _('Display {portfolio}').format(portfolio=str(obj))
        return mark_safe(f'<a href="{href}">{label}</a>')
