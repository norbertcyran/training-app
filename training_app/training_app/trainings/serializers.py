"""Serializers for models."""
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from .models import Exercise, MuscleGroup, Set, WorkoutExercise, Workout


class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = '__all__'
        extra_kwargs = {'slug': {'read_only': True}}


class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer for Exercise model."""
    muscles_involved = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=MuscleGroup.objects.all(),
        many=True,
        help_text=_('Muscles involved in the exercise (use slugs)')
    )

    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Exercise
        fields = '__all__'


class SetSerializer(serializers.ModelSerializer):
    """Serializer for Set model."""
    class Meta:
        model = Set
        fields = ('reps', 'weight', 'order')


class WorkoutExerciseSerializer(serializers.HyperlinkedModelSerializer):
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


class WorkoutSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Workout model."""
    user = serializers.ReadOnlyField(source='user.username')
    exercises = serializers.HyperlinkedIdentityField(
        view_name='workout-exercise-list',
        lookup_url_kwarg='workout_pk'
    )

    class Meta:
        model = Workout
        fields = ('id', 'user', 'date', 'comments', 'exercises')
