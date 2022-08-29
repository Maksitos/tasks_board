import json
from .models import Task
from asyncio import sleep
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class InfoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        for i in range(600):
            info =  sync_to_async(Task.objects.filter(status=4).count)()
            await self.send(json.dumps({'value': str(await info)}))
            await sleep(1)