
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as loginUser
from django.contrib.auth import logout as logoutUser


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            loginUser(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html')

def logout(request):
    logoutUser(request)
    return redirect("index")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        isValid = form.is_valid()
        print("IsValid",isValid)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
            form = UserCreationForm()
    return render(request, 'signup.html')


def system_overview(request):
    return render(request, 'system_overview.html')

def maintenance_schedule(request):
    return render(request, 'maintenance_schedule.html')

@login_required
def maintenance_data_entry(request):
    return render(request, 'maintenance_data_entry.html')

def help_support(request):
    return render(request, 'help_support.html')

@login_required
def ground_floor(request):
    return render(request, 'ground_floor.html')

@login_required
def seven_m(request):
    return render(request, '7m.html')

@login_required
def eleven_m(request):
    return render(request, '11m.html')

@login_required
def dome(request):
    return render(request, 'dome.html')

@login_required
def ext_building(request):
    return render(request, 'extbuilding.html')

