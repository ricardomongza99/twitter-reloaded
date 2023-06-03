from django.shortcuts import render
from .models import Event


def event_feed(request):
    events = Event.objects.order_by('-timestamp')
    return render(request, 'events/event_feed.html', {'events': events})
