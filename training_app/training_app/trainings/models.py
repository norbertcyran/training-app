from django.contrib.auth.models import User
from django.db import models


class MuscleGroup(models.Model):
    """Model representing muscle groups."""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    """Model representing a single exercise. Base building block of the app."""
    name = models.CharField(max_length=50)

    description = models.TextField(max_length=200)

    muscles_involved = models.ManyToManyField(to=MuscleGroup,
                                              related_name='exercises')

    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
