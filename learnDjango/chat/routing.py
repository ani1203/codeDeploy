# chat/routing.py
from django.urls import re_path

from .consumers import ChatConsumer

# routing is to channels as urls are to django
websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', ChatConsumer),
]
