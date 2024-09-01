from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Subscriber(BaseModel):
    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
    )

    class Meta:
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')

    def __str__(self):
        return _('Subscriber {email}').format(email=self.email)
