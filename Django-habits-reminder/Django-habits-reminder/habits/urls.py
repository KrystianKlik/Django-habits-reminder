from django.urls import path
from .views import HabitsListView, HabitsCreateView, HabitsUpdateView, HabitsDeleteView, ChangeHabitStatus

urlpatterns = [
    path('', HabitsListView.as_view(), name='index'),
    path('habits/new/', HabitsCreateView.as_view() , name='habit-create'),
    path('habits/<int:pk>/update/', HabitsUpdateView.as_view() , name='habit-update'),
    path('habits/<int:pk>/delete/', HabitsDeleteView.as_view() , name='habit-delete'),
    #ajax calls
    path('habits/<int:id>/habitstatus', ChangeHabitStatus, name='habit-change-status')
    ]