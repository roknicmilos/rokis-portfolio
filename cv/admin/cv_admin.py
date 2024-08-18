from django.contrib import admin

from cv.admin import EmploymentInline
from cv.models import CV


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    inlines = [
        EmploymentInline,
    ]
