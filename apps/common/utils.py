from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
from django.urls import reverse


def get_model_admin_change_list_url(model_class: type[Model]) -> str:
    content_type = ContentType.objects.get_for_model(model_class)
    return reverse(
        f"admin:{content_type.app_label}_{content_type.model}_changelist"
    )
