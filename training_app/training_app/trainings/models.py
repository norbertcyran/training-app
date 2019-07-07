import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class MuscleGroup(models.Model):
    """Model representing muscle groups."""
    name = models.CharField(
        max_length=50,
        verbose_name=_('Name'),
        help_text=_('Name of the muscle group'),
        unique=True
    )

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ('name', )


def exercise_image_upload(instance, filename):
    return os.path.join('exercise-images', instance.id, filename)


class Exercise(models.Model):
    """Model representing a single exercise. Base building block of the app."""
    name = models.CharField(
        max_length=50,
        verbose_name=_('Exercise name'),
        help_text=_('Name of the exercise')
    )

    description = models.TextField(
        max_length=200,
        verbose_name=_('Exercise description'),
        help_text=_('Instructions on how to perform the exercise')
    )

    muscles_involved = models.ManyToManyField(
        MuscleGroup,
        related_name='exercises',
        verbose_name=_('Muscles involved'),
        help_text=_('Muscles involved in the exercise')
    )

    image = models.ImageField(
        upload_to='exercise-images',
        verbose_name=_('Exercise image'),
        help_text=_('Illustrative image of the exercise'),
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='exercises'
    )

    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Workout(models.Model):
    """Class representing single workout."""
    user = models.ForeignKey(User, related_name='workouts', on_delete=models.CASCADE)

    date = models.DateField(help_text=_('Date when the workout was performed'))

    comments = models.TextField(
        max_length=200,
        verbose_name=_('Comments to the workout'),
        help_text=_('Comments to the workout')
    )


class WorkoutExercise(models.Model):
    """Class representing single exercise in a workout."""
    workout = models.ForeignKey(
        Workout,
        related_name='exercises',
        on_delete=models.CASCADE,
        help_text=_('Workout which the exercise is part of')
    )

    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        verbose_name=_('Exercise'),
        help_text=_('Exercise')
    )


class Set(models.Model):
    """Class representing single set in a workout."""
    workout_exercise = models.ForeignKey(
        WorkoutExercise,
        on_delete=models.CASCADE,
        related_name='sets'
    )

    reps = models.IntegerField(verbose_name=_('Repetitions'))

    weight = models.DecimalField(
        verbose_name=_('Weight'),
        decimal_places=2,
        max_digits=6
    )

    order = models.IntegerField(verbose_name=_('Order'))

    @property
    def exercise(self):
        return self.workout_exercise.exercise

    def __str__(self):
        return f'{self.exercise} - {self.reps} x {self.weight} kg.'

    class Meta:
        ordering = ('order', )
