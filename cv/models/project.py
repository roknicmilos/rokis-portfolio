from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    cv = models.ForeignKey(
        'CV',
        verbose_name=_('CV'),
        on_delete=models.CASCADE,
        related_name='projects',
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=100,
    )
    role = models.CharField(
        verbose_name=_('role'),
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
            'Leave empty if you are currently working on this '
            'project. Day is not important. Select 1st if you '
            'don\'t know the exact end day.'
        ),
    )
    description = models.TextField(
        verbose_name=_('description'),
        default='',
    )
