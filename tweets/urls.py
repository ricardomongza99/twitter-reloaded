from django.urls import path
from . import views
from users import views as userviews

app_name = 'tweets'

urlpatterns = [
    path('', views.home, name='home'),
    path('create-tweet/', views.create_tweet, name='create-tweet'),
    path('tweet/<int:tweet_id>/', views.tweet_thread, name='tweet-thread'),
    path('reply/<int:tweet_id>/', views.create_reply, name='create-reply'),
]