# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from agenda.models import Task
from datetime import date
import pytz

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name', 'id': 'firstname'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name', 'id': 'lastname'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your e-mail', 'id': 'email'}),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Choose a password', 'name': 'password', 'id': 'password'}),
        }

class TaskForm(forms.ModelForm): 
    class Meta: 
        model = Task
        fields=['title', 'description', 'lieu', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'What ?', 'id': 'title'}),
            'description': forms.TextInput(attrs={'placeholder': 'How ? Why ? ', 'id': 'description'}),
            'lieu': forms.TextInput(attrs={'placeholder': 'Where ?', 'id': 'lieu'}),
            'date': forms.DateTimeInput(attrs={'placeholder': 'When ? YYYY-MM-DD HH:MM', 'name': 'date', 'id': 'date'}),
        }

    def clean_date(self):
        date = self.cleaned_data['date']
        if date.date() < date.now(tz=pytz.timezone("Europe/Paris")).date():
            raise forms.ValidationError("The date cannot be in the past!")
        return date