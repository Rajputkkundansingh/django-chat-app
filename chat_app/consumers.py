import json
import os
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from datetime import datetime
import base64

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)

            if data.get('file_name') and data.get('file_data'):
                # File upload via Base64
                file_name = data['file_name']
                file_data = base64.b64decode(data['file_data'])

                upload_dir = os.path.join(settings.MEDIA_ROOT, "uploads")
                os.makedirs(upload_dir, exist_ok=True)

                file_path = os.path.join(upload_dir, file_name)
                with open(file_path, 'wb') as f:
                    f.write(file_data)

                file_url = settings.MEDIA_URL + "uploads/" + file_name

                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': f"File received: {file_url}",
                        'username': data.get('username')
                    }
                )
            else:
                # Normal text message
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': data['message'],
                        'username': data['username']
                    }
                )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username']
        }))
