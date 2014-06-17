# -*- coding: utf-8 -*-
from fabric.api import local

# Desarrollo


def runserver():
    local('python manage.py runserver 0.0.0.0:8000 --settings redcnba.settings.local')


def run():
    local('python manage.py runserver --settings redcnba.settings.local')


def syncdb():
    local('python manage.py syncdb --settings redcnba.settings.local')