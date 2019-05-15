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

    image = models.ImageField(verbose_name=_('Exercise image'), null=True)

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


class WorkoutExercise(models.Model):
    """Class representing single exercise in a workout."""
    workout = models.ForeignKey(Workout, related_name='exercises', on_delete=models.CASCADE)

    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)


class Set(models.Model):
    """Class representing single set in a workout."""
    workout_exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE,
                                         related_name='sets')

    repetitions = models.IntegerField(verbose_name=_('Repetitions'))

    weight = models.DecimalField(verbose_name=_('Weight'), decimal_places=2,
                                 max_digits=6)

    @property
    def exercise(self):
        return self.workout_exercise.exercise

    def __str__(self):
        return f'{self.exercise} - {self.repetitions} x {self.weight} kg.'
