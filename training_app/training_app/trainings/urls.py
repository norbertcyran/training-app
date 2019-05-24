from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'muscle_groups', views.MuscleGroupViewSet)
router.register(r'exercises', views.ExerciseViewSet)
router.register(r'workouts', views.WorkoutViewSet, basename='workout')

urlpatterns = router.urls
