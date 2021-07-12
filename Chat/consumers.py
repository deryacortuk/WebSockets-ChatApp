from channels.generic.websocket import AsyncWebsocketConsumer
import json


class RealTimeChat(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomname = self.scope['url_route']['kwargs']['roomname']
        self.room_group_name = 'chat_%s' % self.roomname

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
        message = text_data_json['message']
        username = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
          'type':'testMessage',
          'message': message,
          'username':username,
            }
        )
    async def testMessage(self,event):

        othervalue = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message':othervalue,
            'username':username,
        }))



    