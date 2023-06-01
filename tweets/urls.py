from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
    path('', views.display_tweets, name='home'),
]