from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    """
    this class different methods for connecting and isconnecting with the
     chat room and also for receiving a message  and is
     also using web-sockets to do so
     All methods are async def rather than just def.

    """
    async def connect(self):
        #  self.scope obtains the 'room_name' parameter from the URL route in chat/routing.py that
        # opened the WebSocket connection to the consumer
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,          # self.room_group_name Constructs a Channels group name directly
            self.channel_name              # from the user-specified room name, without any quoting or escaping.

        )   # if you do not call accept() within the connect() method then the connection will be rejected and closed.

        await self.accept()        # Accepts the WebSocket connection

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,     # self.room_group_name Constructs a Channels group name directly
            self.channel_name       # from the user-specified room name, without any quoting or escaping.
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        # Sends an event to a group(self.channel_layer.group_send())
        await self.channel_layer.group_send(
            self.room_group_name,            # self.room_group_name Constructs a Channels group name directly
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']      # Receive message from room group

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
