from . import views
from django.urls import path

urlpatterns = [
    path("register/", views.register, name="register"),
    # path("register_user/", views.register_user, name="register_user"),
    # path("login/", views.login, name="login"),
]