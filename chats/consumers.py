from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Message,Room
from channels.db import database_sync_to_async
class ChatConsumer(AsyncWebsocketConsumer):

    # Function to save message to database
    @database_sync_to_async
    def save_message(self,user,content,room_slug):
        room = Room.objects.get(slug=room_slug)
        message_save = Message.objects.create(user=user,content=content,room=room)
        message_save.save()

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        username = text_data_json['username']
        message = text_data_json['message']

        room_slug = self.scope['url_route']['kwargs']['room_name']
        await self.save_message(user=self.scope['user'],content=message,room_slug=room_slug)
        
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type":"sendMessage",
                "username":username,
                "message":message
            }
        )
        

    async def sendMessage(self,event):
        username = event['username']
        message = event['message']
        await self.send(text_data=json.dumps(
            {
                "username":username,
                "message":message
            }
        ))
