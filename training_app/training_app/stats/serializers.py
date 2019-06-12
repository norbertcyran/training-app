from rest_framework import serializers

from .models import WeightEntry, ExerciseScoreEntry


class WeightEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeightEntry
        fields = ('id', 'user', 'weight', 'date')


class ExerciseScoreEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExerciseScoreEntry
        fields = ('id', 'user', 'exercise', 'weight', 'date')
