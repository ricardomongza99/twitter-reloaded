from django.urls import path
from . import views
from users import views as userviews


app_name = 'tweets'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', userviews.register, name='register'),
    path('login/', userviews.user_login, name='login')
]