from django.contrib.admin import StackedInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User

from .models import UserProfile


class ProfileInline(StackedInline):
    model = UserProfile


class UserAdmin(BaseUserAdmin):
    inlines = BaseUserAdmin.inlines + [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
