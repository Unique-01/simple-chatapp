from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'saheed'

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
