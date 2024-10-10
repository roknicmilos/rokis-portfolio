from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from apps.user.models import User


def get_default_user_permissions() -> list[Permission]:
    content_type = ContentType.objects.get_for_model(User)

    return [
        Permission.objects.get(codename="view_user", content_type=content_type),
        Permission.objects.get(
            codename="change_user", content_type=content_type
        ),
    ]
