from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("login/", views.login, name="login"),
    # path("user_login/", views.user_login, name="user_login"),
]