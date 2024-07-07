"""
WSGI config for djangobnb_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import sys
import os

sys.path.append('/path/to/your/project')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobnb_backend.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()