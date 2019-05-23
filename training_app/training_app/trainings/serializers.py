"""Serializers for models."""
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
        fields = '__all__'
