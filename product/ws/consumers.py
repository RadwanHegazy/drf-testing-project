from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

class NotificationConsumer(WebsocketConsumer) : 

    def connect(self):
        self.user = self.scope['user']

        if self.user.is_anonymous or self.user.is_superuser is False :
            self.close()
        
        self.accept()
        
        self.GROUP_NAME = f'notification_layer_{self.user.id}'
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME,
            self.channel_name,
        )


    
    def disconnect(self, code):
        if hasattr(self, 'GROUP_NAME') :
            async_to_sync(self.channel_layer.group_discard)(
                self.GROUP_NAME,
                self.channel_name
            )
           

    def notify(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))