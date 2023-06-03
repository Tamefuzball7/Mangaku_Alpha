"""
ASGI config for social_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from mangaku.routing import websocket_urlpatterns
from django.conf import settings
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler

application = get_asgi_application()
application = ASGIStaticFilesHandler(application)



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_project.settings')



application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': (
        URLRouter( websocket_urlpatterns),
        )
    }
)




