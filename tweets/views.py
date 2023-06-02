from django.shortcuts import render, redirect
from .models import Tweet
from django.utils import timezone


# @login_required
def home(request):
    tweets = Tweet.objects.order_by('-created_at')[:10]
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