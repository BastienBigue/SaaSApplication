# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from agenda.forms import UserRegistrationForm, TaskForm
from django.contrib.auth.decorators import login_required
from agenda.models import Agenda, Task
from django.contrib.auth.models import User


# Create your views here.

def homepage(request): 
    return render(request, 'agenda/welcome.html', locals())

def register(request):
    """ Page d'enregistrement d'un nouvel utilisateur """

    # A boolean value for telling the template whether the registration was successful.
    registered = False
    error_registration = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)

        # If the two forms are valid
        if user_form.is_valid():
            # Check same password
            if request.POST['password'] != request.POST['password2']:
                error_registration = True
                error_registration_text = "Passwords should be the same"
                return render(request, 'agenda/user/register.html', locals())

            else:
                # Save info to the database.
                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.email = request.POST['username']
                user.save()

                #authenticate and login directly
                user = authenticate(username=user.email, password=request.POST['password'])
                login(request, user)

                agenda = Agenda.objects.create(user=user, mail=user.email)

                registered = True
                task_form = TaskForm()
                return render(request, 'agenda/addTask.html', locals())

        else:
            error_registration = True
            if not user_form.is_valid():
                error_registration_text = user_form.errors
            return render(request, 'agenda/user/register.html', locals())

    # Not a HTTP POST, so we render our empty form.
    else:
        user_form = UserRegistrationForm()
        return render(request, 'agenda/user/register.html', locals())


def user_login(request):
    """ Gestion login """
    error_login = False

    # Click on SIGN IN
    if request.method == 'POST':
        # Authenticate the user
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        # Test if user exists
        if user:
            login(request, user)
            task_form = TaskForm()
            return redirect('dashboard')
            # return render(request, 'agenda/addTask.html', locals())
        else:
            error_login = True
            return render(request, 'agenda/welcome.html', locals())
    else: 
        task_form = TaskForm()
        return render(request, 'agenda/addTask.html', locals())


        

@login_required(login_url='/agenda/')
def addTask(request):
    new_task_added = False
    form_errors_b = False
    if request.POST:
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.agenda = Agenda.objects.get(user=User.objects.get(username=request.user))
            task.save()
            new_task_added = True 
            task_form = TaskForm()
            return redirect('dashboard')
            # return render(request, 'agenda/addTask.html', locals())
        else: 
            form_errors_b = True
            form_errors = task_form.errors
            return render(request, 'agenda/addTask.html', locals())
    else: 
        task_form = TaskForm(data=request.POST)
        return render(request, 'agenda/addTask.html', locals())


@login_required(login_url='/agenda/')
def dashboard(request):
        userAgenda = Agenda.objects.get(user=User.objects.get(username=request.user))
        taskList=userAgenda.task_set.all()
        return render(request, 'agenda/dashboard.html', locals())


@login_required
def user_logout(request):
    """ Gestion logout """
    logout(request)
    return redirect(reverse(homepage))