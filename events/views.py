from datetime import date
from django.shortcuts import render
from django.db.models import Count, Q
from django.contrib.auth.models import User

from .models import Event
from tweets.models import Tweet


def event_feed(request):
    events = Event.objects.order_by('-timestamp')
    return render(request, 'events/event_feed.html', { 'events': events })


def reports_view(request):

    top_user_today = User.objects.annotate(
        event_count=Count(
            'event', filter=Q(
                event__timestamp__date=date.today()
            )
        )
    ).order_by('-event_count').first()

    most_commented_tweet = Tweet.objects.filter(
        created_at__date=date.today(),
        parent=None  # Only consider original tweets, not replies
    ).annotate(
        num_replies=Count('replies')
    ).order_by('-num_replies').first()

    users_opened_app_today = Event.objects.filter(
        type='OA', timestamp__date=date.today()
    ).values('user').distinct().count()

    context = {
        'top_user_today': top_user_today,
        'most_commented_tweet': most_commented_tweet,
        'users_opened_app_today': users_opened_app_today,
    }

    return render(request, 'events/reports.html', context)
