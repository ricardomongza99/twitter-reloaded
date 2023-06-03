from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    EVENT_TYPES = (
        ('CT', 'Create Tweet'),
        ('RT', 'Reply Tweet'),
        ('OA', 'Open Application'),
    )
    type = models.CharField(max_length=2, choices=EVENT_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)