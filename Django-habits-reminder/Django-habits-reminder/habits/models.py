from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Habits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    days = models.PositiveIntegerField()
    status = models.BooleanField(default = False)
    priority = models.SmallIntegerField(default=1, validators=[MaxValueValidator(10),MinValueValidator(1)])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


