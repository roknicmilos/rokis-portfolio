from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.user.models import User
from django.contrib import admin
from django.contrib.auth.models import Group

# Unregister the Group model from the admin site:
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "portfolio_count",
        "date_joined",
        "last_login",
    )
    readonly_fields = (
        "portfolio_count",
        "created",
        "modified",
        "date_joined",
        "last_login",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                    "created",
                    "modified",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)
