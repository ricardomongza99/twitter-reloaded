from django.db import models
from users.models import User


class Tweet(models.Model):
    content = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    content = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name="reply", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)