from django.contrib import admin

from cv.models import CV


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    pass
