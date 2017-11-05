# -*- coding: utf-8 -*-

from django.conf.urls import url
from meteo import views as local_views
from django.contrib.auth import views as contrib_views

urlpatterns = [

	url(r'^$', local_views.register, name='register'),  

]