from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .serializers import WeightEntrySerializer, ExerciseScoreEntrySerializer
from .models import WeightEntry, ExerciseScoreEntry


class WeightEntryViewSet(ReadOnlyModelViewSet):
    queryset = WeightEntry.objects.all()
    serializer_class = WeightEntrySerializer


class ExerciseScoreEntryViewSet(ReadOnlyModelViewSet):
    queryset = ExerciseScoreEntry.objects.all()
    serializer_class = ExerciseScoreEntrySerializer


class UserWeightEntryViewSet(ModelViewSet):
    serializer_class = WeightEntrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return WeightEntry.objects.filter(user=self.kwargs['user_pk'])


class UserExerciseScoreEntryViewSet(ModelViewSet):
    serializer_class = ExerciseScoreEntrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return ExerciseScoreEntry.objects.filter(user=self.kwargs['user_pk'])
