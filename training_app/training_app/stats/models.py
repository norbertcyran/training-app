from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..trainings.models import Exercise


class WeightEntry(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='weight_entries'
    )

    weight = models.DecimalField(
        verbose_name=_('Weight'),
        decimal_places=1,
        max_digits=4
    )

    date = models.DateField(auto_now_add=True)


class ExerciseScoreEntry(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='records'
    )

    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='record',
        help_text=_('Exercise'),
        verbose_name=_('Exercise')
    )

    weight = models.DecimalField(
        verbose_name=_('Weight'),
        decimal_places=2,
        max_digits=5,
        help_text=_('Weight lifted'),
    )

    date = models.DateField(auto_now_add=True)
