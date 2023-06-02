from django.urls import path
from . import views
from users import views as userviews


urlpatterns = [
    path('', views.home, name='home'),
    path('create-tweet/', views.create_tweet, name='create-tweet'),
]