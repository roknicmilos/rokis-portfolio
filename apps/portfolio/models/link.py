from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Link(BaseModel):
    class Type(models.TextChoices):
        LINKEDIN = 'linkedin', _('LinkedIn')
        GITHUB = 'github', _('GitHub')
        WEBSITE = 'website', _('Website')

    portfolio = models.ForeignKey(
        'Portfolio',
        verbose_name=_('Portfolio'),
        on_delete=models.CASCADE,
        related_name='links',
    )
    type = models.CharField(
        verbose_name=_('type'),
        max_length=10,
        choices=Type.choices,
    )
    label = models.CharField(
        verbose_name=_('label'),
        max_length=100,
    )
    url = models.URLField(
        verbose_name=_('URL'),
    )

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')

    def __str__(self):
        return f'{self.label} ({self.get_type_display()})'
