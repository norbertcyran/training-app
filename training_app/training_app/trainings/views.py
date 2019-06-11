from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import MuscleGroup, Exercise, Workout, WorkoutExercise
from .serializers import MuscleGroupSerializer, ExerciseSerializer, WorkoutSerializer, \
    WorkoutExerciseSerializer


class MuscleGroupViewSet(ModelViewSet):
    """
    list:
    Return all existing muscle groups.
    """
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
    """
    list:
    Return all exercises performed in the workout.

    retrieve:
    Return details of performed exercise.

    create:
    Add exercise to the workout. Sets have to JSON with schema
    `{weight: float, reps: int, order: int}`.

    update:
    Update existing exercise with parameters as in create.

    partial_update:
    Update exercise only with given keys.

    delete:
    Delete the exercise from the workout.
    """
    serializer_class = WorkoutExerciseSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        return WorkoutExercise.objects.filter(workout=self.kwargs['workout_pk'])
