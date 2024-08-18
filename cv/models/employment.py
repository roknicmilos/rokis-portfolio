from django.db import models
from django.utils.translation import gettext_lazy as _


class Employment(models.Model):
    cv = models.ForeignKey(
        'CV',
        verbose_name=_('CV'),
        on_delete=models.CASCADE,
        related_name='employments',
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=100,
    )
    company = models.CharField(
        verbose_name=_('company'),
        max_length=100,
    )
    start = models.DateField(
        verbose_name=_('start'),
        help_text=_(
            'Day is not important. Select 1st if you don\'t '
            'know the exact start day.'
        ),
    )
    end = models.DateField(
        verbose_name=_('end'),
        null=True,
        blank=True,
        help_text=_(
            'Leave empty if you are currently working here. '
            'Day is not important. Select 1st if you don\'t '
            'know the exact end day.'
        ),
    )
    location = models.CharField(
        verbose_name=_('location'),
        max_length=100,
    )
    description = models.TextField(
        verbose_name=_('description'),
    )

    class Meta:
        verbose_name = _('Employment')
        verbose_name_plural = _('Employments')

    def __str__(self):
        return f'{self.title} at {self.company}'
