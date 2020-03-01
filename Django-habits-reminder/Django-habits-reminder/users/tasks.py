from celery import shared_task, task
from time import sleep
from celery.task import periodic_task 
from celery.schedules import crontab
from .models import Profile
from django.contrib.auth.models import User
from celery.contrib import rdb

@task(name='summary') 
#@periodic_task(run_every=crontab(minute="*", hour=0)) # It will run your task at midnight
def SetCurrentStrikeToZero():

    users = User.objects.all()
    #If user didn't done all habits his current strike equal 0
    for user in users:
        user.profile.current_strike_count = 0
        rdb.set_trace()
        

    
