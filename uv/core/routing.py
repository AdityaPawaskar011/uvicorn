from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path,path
from core.consumers import NotificationConsumer

# websocket_urlpatterns = [
#      re_path(r"ws?notifications/$",NotificationConsumer.as_asgi()),
# ]


# from core.consumers import MyConsumer
websocket_urlpatterns = [
    path('ws/ac_websocket/',NotificationConsumer.as_asgi()),
]