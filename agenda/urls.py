# -*- coding: utf-8 -*-

from django.conf.urls import url
from agenda import views as local_views
from django.contrib.auth import views as contrib_views

urlpatterns = [
	url(r'^$', local_views.homepage, name='homepage'),  
	url(r'^register', local_views.register, name='register'),  
	url(r'^login', local_views.user_login, name='login'),  
	url(r'^dashboard', local_views.dashboard, name='dashboard'),  
	url(r'^logout', local_views.user_logout, name='logout'),
	url(r'^addTask', local_views.addTask, name='addTask'),

]