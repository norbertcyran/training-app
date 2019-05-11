from django.urls import path
import knox.views as knox_views

from .views import LoginView, CurrentUserView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logout-all/', knox_views.LogoutAllView.as_view(), name='knox_logout_all'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', CurrentUserView.as_view(), name='current_user')
]
