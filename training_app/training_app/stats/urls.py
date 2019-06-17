from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from . import views
from ..accounts.urls import router as accounts_router

router = DefaultRouter()
router.register(r'weight_entries', views.WeightEntryViewSet)
router.register(r'exercise_score_entries', views.ExerciseScoreEntryViewSet)

user_entries_router = NestedSimpleRouter(accounts_router, r'users', lookup='user')
user_entries_router.register(
    'weight_entries',
    viewset=views.UserWeightEntryViewSet,
    basename='user-weight-entry'
)
user_entries_router.register(
    'exercise_entries',
    viewset=views.UserExerciseScoreEntryViewSet,
    basename='user-exercise-entry'
)

urlpatterns = router.urls + user_entries_router.urls
