from django.db import models
from django.utils.translation import gettext_lazy as _


class CV(models.Model):
    slug = models.SlugField(
        verbose_name=_('slug'),
        max_length=100,
        unique=True,
    )
    title = models.CharField(
        verbose_name=_('title'),
        max_length=100,
    )
    filename = models.CharField(
        verbose_name=_('filename'),
        max_length=100,
    )
    avatar = models.ImageField(
        verbose_name=_('avatar'),
        upload_to='cv/img/',
        null=True,
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=50,
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=50,
    )
    role = models.CharField(
        verbose_name=_('role'),
        max_length=100,
    )
    email = models.EmailField(
        verbose_name=_('email'),
        max_length=100,
    )
    phone = models.CharField(
        verbose_name=_('phone'),
        max_length=20,
    )
    address_label = models.CharField(
        verbose_name=_('address label'),
        max_length=100,
    )
    address_link = models.URLField(
        verbose_name=_('address link'),
        max_length=1000,
    )
    about_me = models.TextField(
        verbose_name=_('about me'),
    )

    class Meta:
        verbose_name = _('CV')
        verbose_name_plural = _('CVs')

    def __str__(self):
        return self.title

    @property
    def ordered_employments(self) -> models.QuerySet:
        return self.employments.order_by('-start')

    @property
    def ordered_internships(self) -> models.QuerySet:
        return self.internships.order_by('-start')

    @property
    def ordered_educations(self) -> models.QuerySet:
        return self.educations.order_by('-start')
