
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as loginUser
from django.contrib.auth import logout as logoutUser
from .models import DOTComponents, DOT_Maintenance, DOT_Systems
import sqlite3



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

def gf_pnumatical(request):
    connection = sqlite3.connect("DOT_Maintenance.db")
    print(connection)
    rows = connection.execute("SELECT Sr_no, Systems, Units, Components, Replacement_Due, Failure_Mode FROM DOT_Components where Systems = 'Pnumatical System '")
    row_list = []
    for x in rows:
        obj = DOTComponents(x[0],x[1],x[2],x[3],x[4],x[5])
        row_list.append(obj)
    connection.close()

    return render(request, 'gf_pnumatical.html',{"gf_data":row_list})

def gf_hydraulic (request):
    connection = sqlite3.connect("DOT_Maintenance.db")
    print(connection)
    rows = connection.execute("SELECT Sr_no, Systems, Units, Components, Replacement_Due, Failure_Mode FROM DOT_Components where Systems = 'Hydraulic System '")
    row_list = []
    for x in rows:
        obj = DOTComponents(x[0],x[1],x[2],x[3],x[4],x[5])
        row_list.append(obj)
    connection.close()

    return render(request, 'gf_hydraulic.html',{"gf_data":row_list})

def gf_cooling (request):
    connection = sqlite3.connect("DOT_Maintenance.db")
    print(connection)
    rows = connection.execute("SELECT Sr_no, Systems, Units, Components, Replacement_Due, Failure_Mode FROM DOT_Components where Systems = 'Cooling System '")
    row_list = []
    for x in rows:
        obj = DOTComponents(x[0],x[1],x[2],x[3],x[4],x[5])
        row_list.append(obj)
    connection.close()

    return render(request, 'gf_cooling.html',{"gf_data":row_list})

def gf_maintenance(request):
    connection = sqlite3.connect("DOT_Maintenance.db")
    print(connection)
    rows = connection.execute("SELECT * FROM DOT_Maintenance where levels like '%GF%'")
    row_list = []
    for x in rows:
        obj = DOT_Maintenance(x[0],x[1],x[2],x[3])
        row_list.append(obj)
    connection.close()

    return render(request, 'gf_maintenance.html',{"gf_maintenance":row_list})

def seven_system(request):
    connection = sqlite3.connect("DOT_Maintenance.db")
    print(connection)
    rows = connection.execute("SELECT Sr_no, Systems, Components, Replacement_Due, Failure_Mode FROM DOT_Systems where Floor = '7m '")
    row_list = []
    for x in rows:
        obj = DOT_Systems(x[0],x[1],x[2],x[3],x[4])
        row_list.append(obj)
    connection.close()

    return render(request, '7m_system.html',{"gf_data":row_list})

def seven_maintenance(request):
    connection = sqlite3.connect("DOT_Maintenance.db")
    print(connection)
    rows = connection.execute("SELECT * FROM DOT_Maintenance where levels like '%7%'")
    row_list = []
    for x in rows:
        obj = DOT_Maintenance(x[0],x[1],x[2],x[3])
        row_list.append(obj)
    connection.close()

    return render(request, '7m_maintenance.html',{"7m_maintenance":row_list})

def eleven_system(request):
    connection = sqlite3.connect("DOT_Maintenance.db")
    print(connection)
    rows = connection.execute("SELECT Sr_no, Systems, Components, Replacement_Due, Failure_Mode FROM DOT_Systems where Floor = '11m '")
    row_list = []
    for x in rows:
        obj = DOT_Systems(x[0],x[1],x[2],x[3],x[4])
        row_list.append(obj)
    connection.close()

    return render(request, '11m_system.html',{"gf_data":row_list})

def eleven_maintenance(request):
    connection = sqlite3.connect("DOT_Maintenance.db")
    print(connection)
    rows = connection.execute("SELECT * FROM DOT_Maintenance where levels like '%11%'")
    row_list = []
    for x in rows:
        obj = DOT_Maintenance(x[0],x[1],x[2],x[3])
        row_list.append(obj)
    connection.close()

    return render(request, '11m_maintenance.html',{"11m_maintenance":row_list})