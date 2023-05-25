from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Post

class LikeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        post_id = text_data
        await self.toggle_like(post_id)

    @database_sync_to_async
    def toggle_like(self, post_id):
        post = Post.objects.get(id=post_id)
        if self.scope['user'] in post.likes.all():
            post.likes.remove(self.scope['user'])
        else:
            post.likes.add(self.scope['user'])
            post.dislikes.remove(self.scope['user'])

class DislikeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        post_id = text_data
        await self.toggle_dislike(post_id)

    @database_sync_to_async
    def toggle_dislike(self, post_id):
        post = Post.objects.get(id=post_id)
        if self.scope['user'] in post.dislikes.all():
            post.dislikes.remove(self.scope['user'])
        else:
            post.dislikes.add(self.scope['user'])
            post.likes.remove(self.scope['user'])
