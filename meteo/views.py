# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from meteo.forms import UserRegistrationForm

# Create your views here.


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
                error_registration_text = "Passwords are the same"

            else:
                # Save info to the database.
                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.email = request.POST['username']
                user.save()

                # authenticate and login directly
                #user = authenticate(username=request.POST['username'], password=request.POST['password'])
                #login(request, user)

                registered = True

        else:
            error_registration = True
            if not user_form.is_valid():
                error_registration_text = user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    else:
        user_form = UserRegistrationForm()

    return render(request, 'meteo/user/register.html', locals())