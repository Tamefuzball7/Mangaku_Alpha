from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async 


class LikesAndDislikesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'likes_and_dislikes'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def update_counts(self, event):
        likes = event['likes']
        dislikes = event['dislikes']
        await self.send(text_data=f'{{"likes": {likes}, "dislikes": {dislikes}}}')
