from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Subscriber(BaseModel):
    email = models.EmailField(
        verbose_name=_("email address"),
        unique=True,
    )
    submission_count = models.PositiveIntegerField(
        verbose_name=_("submission count"),
        default=1,
    )

    class Meta:
        verbose_name = _("Subscriber")
        verbose_name_plural = _("Subscribers")

    def __str__(self):
        return _("Subscriber {email}").format(email=self.email)

    def update(self, **kwargs):
        for field_name, field_value in kwargs.items():
            setattr(self, field_name, field_value)
        self.save()
