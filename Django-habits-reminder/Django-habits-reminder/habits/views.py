from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Habits


class HabitsListView(ListView):
    model = Habits
    template_name = 'habits/index.html'
    context_object_name = 'habits'
    ordering = ['priority']

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user).filter(implement=True)

class HabitsCreateView(LoginRequiredMixin, CreateView):
    model = Habits
    fields = ['name', 'days', 'priority']

    def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)


class HabitsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Habits
    fields = ['name', 'days', 'priority']

    def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)

    def test_func(self):
         habits = self.get_object()
         if self.request.user == habits.user:
             return True
         return False


class HabitsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Habits
    success_url = '/'

    def test_func(self):
         habits = self.get_object()
         if self.request.user == habits.user:
             return True
         return False

@csrf_exempt
def ChangeHabitStatus(request, id):
    model = Habits.objects.get(pk = id)
    if(model.status == True):
        model.status=False
    else:
        model.status=True
    model.save()
    return redirect('index') 