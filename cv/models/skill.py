from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Skill(models.Model):
    cv = models.ForeignKey(
        'CV',
        verbose_name=_('cv'),
        on_delete=models.CASCADE,
        related_name='skills',
    )
    label = models.CharField(
        verbose_name=_('label'),
        max_length=100,
    )
    level = models.PositiveSmallIntegerField(
        verbose_name=_('level'),
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    class Meta:
        verbose_name = _('skill')
        verbose_name_plural = _('skills')

    def __str__(self):
        return f'{self.label} ({self.level}/5)'
