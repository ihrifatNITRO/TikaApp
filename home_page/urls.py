from django.urls import path
from . import views
# from home_page import views also works same


urlpatterns = [
    path('', views.index),
    path("home/", views.home, name="home"),
]
