from django.urls import path
from . import views
from users import views as userviews

app_name = 'tweets'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tweet/<int:tweet_id>/', views.tweet_thread_view, name='tweet-thread'),
    path('create-tweet/', views.create_tweet, name='create-tweet'),
    path('reply/<int:tweet_id>/', views.create_reply, name='create-reply'),
]