from django.contrib import admin

from apps.user.models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'created',
        'modified',
    )
    search_fields = (
        'email',
    )
    fields = (
        'id',
        'email',
        'created',
        'modified',
    )
    readonly_fields = (
        'id',
        'created',
        'modified',
    )
