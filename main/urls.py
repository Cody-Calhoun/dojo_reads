from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create_user', views.create_user),
    path('user/dashboard', views.dashboard),
    path('user/login', views.login)
]