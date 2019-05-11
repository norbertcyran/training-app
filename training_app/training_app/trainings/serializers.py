"""Serializers for models."""
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Exercise, MuscleGroup


class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = ('id', 'name')


class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer for Exercise model."""
    class Meta:
        model = Exercise
        fields = ('id', 'name', 'description', 'muscles_involved', 'created_by')
