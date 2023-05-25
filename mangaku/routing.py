from django.urls import re_path
from .consumers import LikeConsumer, DislikeConsumer

websocket_urlpatterns = [
    re_path(r'ws/like/$', LikeConsumer.as_asgi()),
    re_path(r'ws/dislike/$', DislikeConsumer.as_asgi()),
]
