from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_feed_view, name='event-feed'),
    path('reports/', views.reports_view, name='reports'),
]