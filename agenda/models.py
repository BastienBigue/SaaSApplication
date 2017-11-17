# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Agenda(models.Model): 
	user = models.ForeignKey(User)
	mail = models.EmailField()

class Task(models.Model): 
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=300)
	lieu = models.TextField(max_length=300)
	date = models.DateTimeField(null=True, blank=True)
	agenda = models.ForeignKey(Agenda)
