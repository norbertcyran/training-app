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

    primary_muscles = models.ManyToManyField(MuscleGroup,
                                             related_name='exercises',
                                             verbose_name=_('Primary muscles involved'))

    secondary_muscles = models.ManyToManyField(MuscleGroup,
                                               verbose_name=_('Secondary muscles involved'),
                                               related_name='secondary')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exercises')

    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Workout(models.Model):
    """Class representing single workout."""
    user = models.ForeignKey(User, related_name='workouts', on_delete=models.CASCADE)

    date = models.DateField()

    comments = models.TextField(max_length=200,
                                verbose_name=_('Comments to the workout'))


class ExerciseSet(models.Model):
    """Class representing single set in a workout."""
    workout = models.ForeignKey(Workout, related_name='sets', on_delete=models.CASCADE)

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    repetitions = models.IntegerField(verbose_name=_('Repetitions'))

    weight = models.DecimalField(verbose_name=_('Weight'), decimal_places=2,
                                 max_digits=6)

    def __str__(self):
        return f'{self.exercise} - {self.repetitions} x {self.weight} kg.'
