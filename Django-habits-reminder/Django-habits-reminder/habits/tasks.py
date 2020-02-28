from celery import shared_task
from time import sleep
from celery.task import periodic_task 
from celery.schedules import crontab
from .models import Habits
from django.contrib.auth.models import User

#All habits are reseted
@periodic_task(run_every=crontab(minute=10, hour=0)) # It will run your task at midnight
def reset_habbits_status(): 
    habits = Habits.objects.all().update(status=False)
    habits.save()


#    habitsCount =  Habits.objects.all().count()
#    doneHabits = Habits.objects.filter().count()
#    profile = User.Profile.current_strike_count
#    if(habitsCount == doneHabits):
#        profile = profile + 1
#    else:
#        profile = 0

#    profile.save()
#    habits = Habits.objects.all().update(status=False)
#    habits.save()
