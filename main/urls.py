from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create_user', views.create_user),
    path('user/dashboard', views.dashboard),
    path('user/login', views.login),
    path('book/create', views.create_book),
    path('book/book_form', views.book_form),
    path('book/<int:book_id>', views.show_book),
    path('book/add_review', views.add_review),
]