from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import MuscleGroup, Exercise, Workout, WorkoutExercise
from .serializers import MuscleGroupSerializer, ExerciseSerializer, WorkoutSerializer, \
    WorkoutExerciseSerializer


class MuscleGroupViewSet(ModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class WorkoutViewSet(ModelViewSet):
    serializer_class = WorkoutSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutExerciseViewSet(ModelViewSet):
    serializer_class = WorkoutExerciseSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return WorkoutExercise.objects.filter(workout=self.kwargs['workout_pk'])
