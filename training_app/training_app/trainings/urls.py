from rest_framework import routers
from rest_framework_nested.routers import NestedSimpleRouter

from . import views

router = routers.DefaultRouter()
router.register(r'muscle_groups', views.MuscleGroupViewSet)
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'workouts', views.WorkoutViewSet, basename='workout')

exercises_router = NestedSimpleRouter(router, r'workouts', lookup='workout')
exercises_router.register(
    r'exercises',
    viewset=views.WorkoutExerciseViewSet,
    basename='workout-exercise'
)


urlpatterns = router.urls + exercises_router.urls
