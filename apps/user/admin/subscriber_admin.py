from django.contrib import admin

from apps.user.models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'submission_count',
        'created',
        'modified',
    )
    search_fields = (
        'email',
    )
    fields = (
        'id',
        'email',
        'submission_count',
        'created',
        'modified',
    )
    readonly_fields = (
        'id',
        'created',
        'modified',
        'submission_count',
    )
