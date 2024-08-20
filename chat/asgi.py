import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter #Se debe importar
from channels.auth import AuthMiddlewareStack # se debe importar
import app.routing #se importa de la app nuestro archivo routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat.settings')


application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    "websocket": AuthMiddlewareStack( 
    URLRouter( app.routing.websocket_urlpatterns))
    
    })
















