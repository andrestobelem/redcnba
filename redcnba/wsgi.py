"""
WSGI config for redcnba project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

with open('../settings.txt') as f:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f.read().strip())

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
