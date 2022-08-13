"""
ASGI config for mcf_knust_edu_gh_rebuild project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mcf_knust_edu_gh_rebuild.settings')

application = get_asgi_application()
