from celery import shared_task
from time import sleep
from celery.task import periodic_task 
from celery.schedules import crontab
from .models import Profile
from django.contrib.auth.models import User

@periodic_task(run_every=crontab(minute=0, hour=0)) # It will run your task at midnight
def schedule_task():

    users = User.objects.all()
    #If user didn't done all habits his current strike equal 0
    for user in users:
        if user.habits.status == False:
            user.profile.current_strike_count = 0
        #else:
            # If user did done all habits then it adds +1 to current strike plus checks if current strike is bigger then longest recored strike
            #user.profile.current_strike_count =  user.profile.current_strike_count + 1
            #if user.profile.longest_strike > user.profile.current_strike_count:
            #    user.profile.longest_strike = user.profile.current_strike_count
    
