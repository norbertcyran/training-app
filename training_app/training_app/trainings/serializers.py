"""Serializers for models."""
from rest_framework import serializers

from .models import Exercise, MuscleGroup, Set, WorkoutExercise


class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = ('id', 'name')


class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer for Exercise model."""
    class Meta:
        model = Exercise
        fields = '__all__'


class SetSerializer(serializers.ModelSerializer):
    """Serializer for Set model."""
    class Meta:
        model = Set
        fields = ('reps', 'weight', 'order')


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    """Serializer for WorkoutExercise model."""
    sets = SetSerializer(many=True)

    class Meta:
        model = WorkoutExercise
        fields = ('workout', 'exercise', 'sets')

    def create(self, validated_data):
        sets = validated_data.pop('sets')

        workout_exercise = WorkoutExercise.objects.create(**validated_data)

        for set_obj in sets:
            Set.objects.create(workout_exercise=workout_exercise, **set_obj)

        return workout_exercise
