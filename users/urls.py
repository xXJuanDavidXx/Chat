from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name="users/login.html"),
        name = "login"
        ),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', register.as_view(), name="signup"),   
    ]

