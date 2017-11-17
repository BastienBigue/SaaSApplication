# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from agenda.models import Task, Agenda

# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'lieu', 'date')
#     search_fields = ('title', 'lieu')
#     ordering = ('title',)




admin.site.register(Task)
admin.site.register(Agenda)