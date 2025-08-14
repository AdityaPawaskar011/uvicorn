import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer,AsyncWebsocketConsumer

# class NotificationConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         # return await super().connect()
#         if self.user.is_authenticate and self.user.is_staff:
#             await self.channel_layer.group_add("Notifications_staff",self.channel_name)
#         else:
#             await self.channel_layer.group_add("Notification_all",self.channel_name)
#         await self.accept()

#     async def disconnect(self, code):
#         if self.user.is_authenticate and self.user.is_staff:
#             await self.channel_layer.group_add("Notifications_staff",self.channel_name)
#         else:
#             await self.channel_layer.group_add("Notification_all",self.channel_name)
    
#     async def receive(self, text_data):
#         pass

#     async def notify(self,event):
#         await self.send(text_data=json.dumps({"message": event["message"]}))


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("demo")
        await self.send(text_data=json.dumps({"message": "Connected successfully"}))

    async def disconnect(self, close_code):
        print(f"Disconnected: {close_code}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(f"Received: {data}")
        while True:
            
            await self.send(text_data=json.dumps({"message": "Echo: " + data.get("message", "")}))
