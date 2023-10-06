from . import views
from django.urls import path


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/',views.LogoutPage,name='logout'),
    path('update_child/<int:child_id>/', views.update_child, name='update_child'),
]