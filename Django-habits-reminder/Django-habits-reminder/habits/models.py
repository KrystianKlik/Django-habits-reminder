from django.db import models
from django.contrib.auth.models import User



class Habits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    days = models.PositiveIntegerField()

    def __str__(self):
        return self.name
