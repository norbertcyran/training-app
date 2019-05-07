from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class MuscleGroup(models.Model):
    """Model representing muscle groups."""
    name = models.CharField(max_length=50,
                            verbose_name=_('Name'),
                            help_text=_('Name of a muscle group'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Exercise(models.Model):
    """Model representing a single exercise. Base building block of the app."""
    name = models.CharField(max_length=50,
                            verbose_name=_('Exercise name'),
                            help_text=_('Name of an exercise'))

    description = models.TextField(max_length=200,
                                   verbose_name=_('Exercise description'),
                                   help_text=_('Instructions on how to perform an exercise'))

    muscles_involved = models.ManyToManyField(MuscleGroup,
                                              related_name='exercises',
                                              verbose_name=_('Muscles involved'))

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
