from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    ]

    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
        null=False
    )

    avatar = models.ImageField(
        upload_to='user-avatars',
        verbose_name=_('Profile picture'),
        null=True,
        blank=True
    )

    birthday = models.DateField(verbose_name=_('Date of birth'))

    height = models.IntegerField(
        verbose_name=_('Height (cm)'),
        blank=False,
        null=True,
        validators=[MinValueValidator(100), MaxValueValidator(250)]
    )

    gender = models.CharField(
        verbose_name=(_('Gender')),
        blank=False,
        null=True,
        choices=GENDER_CHOICES
    )
