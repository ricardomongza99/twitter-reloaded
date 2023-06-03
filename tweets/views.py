from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tweet
from events.models import Event
from django.utils import timezone


@login_required
def home_view(request):
    tweets = Tweet.objects.filter(parent__isnull=True).order_by('-created_at')[:10]
    return render(request, 'tweets/home.html', {'tweets': tweets})


@login_required
def create_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user
        created_at = timezone.now()

        Tweet.objects.create(content=content, user=user, created_at=created_at)
        Event.objects.create(type='CT', user=request.user)

    return redirect('home')


@login_required
def tweet_thread_view(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    replies = Tweet.objects.filter(parent=tweet)
    return render(request, 'tweets/thread.html', {'tweet': tweet, 'replies': replies})


@login_required
def create_reply(request, tweet_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user
        created_at = timezone.now()

        Tweet.objects.create(content=content, user=user, created_at=created_at, parent_id=tweet_id)
        Event.objects.create(type='RT', user=request.user)

    return redirect('tweet-thread', tweet_id=tweet_id)

