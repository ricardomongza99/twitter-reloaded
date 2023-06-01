from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username



