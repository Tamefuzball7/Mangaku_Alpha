from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
re_path(r'ws/likes_and_dislikes/$', consumers.LikesAndDislikesConsumer.as_asgi()),
]
