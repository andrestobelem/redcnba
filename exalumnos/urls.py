# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from exalumnos import views

urlpatterns = patterns(
    'exalumnos',
    url(r'^$|^home', views.home, name='home'),
)