from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    ACTION_CHOICES = (
        ('CT', 'Create Tweet'),
        ('RT', 'Reply Tweet'),
        ('OA', 'Open Application'),
    )
    action = models.CharField(max_length=2, choices=ACTION_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)