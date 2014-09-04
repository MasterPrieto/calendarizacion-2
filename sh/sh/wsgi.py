"""
WSGI config for sh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/opt/djangostack-1.5.9-0/apps/django/django_projects/sh')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
