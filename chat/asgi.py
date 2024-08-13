"""
ASGI config for chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter #actúa como un enrutador que direcciona las solicitudes según el protocolo que utilizan, como HTTP, WebSocket, entre otros.


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')

#application = get_asgi_application()


application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    })
















