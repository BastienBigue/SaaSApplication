# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from agenda.models import Task, Agenda

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'lieu', 'date')
    search_fields = ('title', 'lieu')
    ordering = ('title',)

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('user', 'mail')
    search_fields = ('user', 'mail')
    ordering = ('user',)




admin.site.register(Task, TaskAdmin)
admin.site.register(Agenda, AgendaAdmin)