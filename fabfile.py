# -*- coding: utf-8 -*-
from fabric.api import local

# Desarrollo


def runserver():
    local('python manage.py runserver 0.0.0.0:8000')


def run():
    local('python manage.py runserver')


def syncdb():
    local('python manage.py syncdb --noinput')