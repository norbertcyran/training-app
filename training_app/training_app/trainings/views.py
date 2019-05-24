from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import MuscleGroup, Exercise, Workout
from .serializers import MuscleGroupSerializer, ExerciseSerializer, WorkoutSerializer


class MuscleGroupViewSet(ModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class WorkoutViewSet(ModelViewSet):
    serializer_class = WorkoutSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
