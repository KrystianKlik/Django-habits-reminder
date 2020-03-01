from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from .models import Habits


def index(request):
    return render(request, 'habits/index.html')


class HabitsListView(ListView):
    model = Habits
    template_name = 'habits/habits.html'
    context_object_name = 'habits'

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user).filter(implement=True).order_by('-priority')

class HabitsListSetup(ListView):
    model = Habits
    template_name = 'habits/habits-list.html'
    context_object_name = 'habits'

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user).order_by('-implement' ,'-priority')

class HabitsCreateView(LoginRequiredMixin, CreateView):
    model = Habits
    fields = ['name',  'priority']
    success_url = '/habits/list/'

    def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)


class HabitsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Habits
    fields = ['name', 'priority']
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
    model = Habits.objects.get(pk = id)
    if(model.status == True):
        model.status=False
    else:
        model.status=True
    model.save()
    return redirect('habits-list') 

@csrf_exempt
def ChangeImplementStatus(request, id):
    habits = Habits.objects.filter(user = request.user.id)
    selectedHabit = Habits.objects.get(pk = id)
     
    if(selectedHabit.implement == True):
        selectedHabit.implement=False
    else:
        selectedHabit.implement=True
    selectedHabit.save()

    habitsCount = habits.filter(implement = True).count()
    #Update habits quantity on profile page
    profile = request.user.profile
    profile.habits_quantity = habitsCount
    profile.save()
    return redirect('habits-list') 


@csrf_exempt
def AllHabitsAreCompleted(request):
    profile = request.user.profile
    habits = Habits.objects.filter(user = request.user)

    allDoneHabits = habits.filter(status = True).count()
    allHabits = habits.count()
 
    if allHabits == allDoneHabits:
        # If user did done all habits then it adds +1 to current strike plus checks if current strike is bigger then longest recored strike
        profile.current_strike_count =  profile.current_strike_count + 1
        if profile.longest_strike < profile.current_strike_count:
            profile.longest_strike = profile.current_strike_count
        profile.did_all_habits = True

    elif profile.did_all_habits == True:
        profile.current_strike_count =  profile.current_strike_count - 1
        if profile.longest_strike > profile.current_strike_count:
            profile.longest_strike = profile.current_strike_count
        profile.did_all_habits = False

    profile.save()
    return redirect('habits-list') 
    
