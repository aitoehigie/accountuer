from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse, reverse_lazy

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

    def get_absolute_url(self):
        return revere_lazy('home')


