from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from .models import MuscleGroup, Exercise
from .serializers import MuscleGroupSerializer, ExerciseSerializer


class MuscleGroupViewSet(ModelViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
