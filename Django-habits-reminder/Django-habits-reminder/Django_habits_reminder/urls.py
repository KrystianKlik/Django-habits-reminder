"""
Definition of urls for Django_habits_reminder.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
#from app import forms, views
from users import views  as users
from habits import views as habits

urlpatterns = [
    path('register', users.register, name='register'),
    path("", users.login, name='login'),
]
