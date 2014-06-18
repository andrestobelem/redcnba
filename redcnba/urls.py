# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', 'exalumnos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^exalumnos/', include('exalumnos.urls', namespace="exalumnos")),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
