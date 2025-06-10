# core/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
import json
from datetime import datetime

class DroneConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("drones", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("drones", self.channel_name)

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            "drones",
            {
                "type": "send_update",
                "message": text_data
            }
        )

    async def send_update(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))

class AlertConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("alerts", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("alerts", self.channel_name)

    async def receive(self, text_data):
        pass  # Client doesn't send; only receives

    async def send_alert(self, event):
        await self.send(text_data=json.dumps(event["alert"]))