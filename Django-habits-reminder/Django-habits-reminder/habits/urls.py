from django.urls import path
from .views import (HabitsListView, HabitsCreateView, HabitsUpdateView, HabitsDeleteView, 
                    ChangeHabitStatus, HabitsListSetup, ChangeImplementStatus, 
                    AllHabitsAreCompleted)

urlpatterns = [
    path('', HabitsListView.as_view(), name='habits'),
    path('list/', HabitsListSetup.as_view(), name='habits-list'),
    path('new/', HabitsCreateView.as_view() , name='habit-create'),
    path('<int:pk>/update/', HabitsUpdateView.as_view() , name='habit-update'),
    path('<int:pk>/delete/', HabitsDeleteView.as_view() , name='habit-delete'),
    #ajax calls
    path('<int:id>/habitstatus', ChangeHabitStatus, name='habit-change-status'),
    path('<int:id>/implementstatus', ChangeImplementStatus, name='habit-change-implement'),
    path('allhabbitsarecompleted/', AllHabitsAreCompleted, name="habits-all-completed" ),
    ]