from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.get_all_players, name='get_all_players'),
]
