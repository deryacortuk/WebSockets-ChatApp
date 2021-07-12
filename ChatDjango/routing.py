from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import re_path
from Chat import consumers

wsUrlPatterns =[ re_path(r'ws/chat/(?P<roomname>\w+)/$',consumers.RealTimeChat.as_asgi()),]


application=ProtocolTypeRouter({
 'websocket':AuthMiddlewareStack(URLRouter(wsUrlPatterns))
})