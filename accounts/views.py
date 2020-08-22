from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm
from .decorators import unauthenticated_user

# Create your views here.


@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created.')
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


@unauthenticated_user
def loginMe(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid username or password')
    return render(request, 'login.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {})


def logoutMe(request):
    logout(request)
    return redirect('login')
