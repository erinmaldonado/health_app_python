"""Defines URL patterns for health_app."""

from django.urls import path

from . import views

app_name = 'health_app'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
]
