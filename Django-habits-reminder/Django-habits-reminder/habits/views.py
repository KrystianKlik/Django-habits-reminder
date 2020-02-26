from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.management.base import NoArgsCommand
from .models import Habits

# Wiem że to nie jest dobre rozwiązanie w następnym projekcie o wiele lepiej bym to rozwiązał w sensie całą architekturę
import sys
sys.path.append("..")
from users.models import Profile



def index(request):
    return render(request, 'habits/index.html')


class HabitsListView(ListView):
    model = Habits
    template_name = 'habits/habits.html'
    context_object_name = 'habits'
    ordering = ['priority' ]

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user).filter(implement=True)

class HabitsListSetup(ListView):
    model = Habits
    template_name = 'habits/habits-list.html'
    context_object_name = 'habits'
    ordering = ['priority', 'implement']

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user)

class HabitsCreateView(LoginRequiredMixin, CreateView):
    model = Habits
    fields = ['name', 'days', 'priority']
    success_url = '/habits/list/'

    def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)


class HabitsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Habits
    fields = ['name', 'days', 'priority']
    success_url = '/habits/list/'

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
    success_url = 'habits/list'

    def test_func(self):
         habits = self.get_object()
         if self.request.user == habits.user:
             return True
         return False

@csrf_exempt
def ChangeHabitStatus(request, id):
    
    profile = request.user.profile.current_strike_count + 1
    profile.save()

    model = Habits.objects.get(pk = id)
    if(model.status == True):
        model.status=False
    else:
        model.status=True
    model.save()
    return redirect('habits-list') 

@csrf_exempt
def ChangeImplementStatus(request, id):
    model = Habits.objects.get(pk = id)
    if(model.implement == True):
        model.implement=False
    else:
        model.implement=True
    model.save()
    return redirect('habits-list') 

def AllHabitsAreDone():
    pass

