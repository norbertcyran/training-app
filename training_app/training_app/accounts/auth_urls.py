from django.urls import path
from knox import views as knox_views

from .views import LoginView, RegisterView, CurrentUserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logout-all/', knox_views.LogoutAllView.as_view(), name='knox_logout_all'),
    path('register/', RegisterView.as_view(), name='register'),
    path('current-user/', CurrentUserView.as_view(), name='current_user')
]

