from django.shortcuts import render, redirect, get_object_or_404
from .models import Tweet
from django.utils import timezone


# @login_required
def home(request):
    tweets = Tweet.objects.filter(parent__isnull=True).order_by('-created_at')[:10]
    return render(request, 'tweets/home.html', {'tweets': tweets})


# @login_required
def create_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user
        created_at = timezone.now()

        tweet = Tweet(content=content, user=user, created_at=created_at)
        tweet.save()

        return redirect('home')
    else:
        return redirect('home')


def tweet_thread(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    replies = Tweet.objects.filter(parent=tweet)
    return render(request, 'tweets/thread.html', {'main_tweet': tweet, 'replies': replies})