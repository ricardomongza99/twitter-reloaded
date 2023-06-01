from django.shortcuts import render, redirect
from .forms import RegistreForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def register(request):
    if request.method  == 'POST':
        form = RegistreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistreForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'users/login.html',)
