from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Habits


class PostListView(ListView):
    model = Habits
    template_name = 'habits/index.html'
    context_object_name = 'habits'

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user)
