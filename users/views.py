from django.shortcuts import render, redirect
from .forms import RegistreForm

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
