from django.shortcuts import render
from .models import Tweet

def display_tweets(request):
    tweets = Tweet.objects.order_by('-created_at')[:10]

    return render(request, 'tweets/tweets.html', {'tweets': tweets})
