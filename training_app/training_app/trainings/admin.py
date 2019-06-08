from django.contrib import admin

from .models import MuscleGroup, Exercise, Workout

admin.site.register(MuscleGroup)
admin.site.register(Exercise)
admin.site.register(Workout)
