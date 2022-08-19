import json
from .models import Task
from time import sleep
from channels.generic.websocket import WebsocketConsumer


class InfoConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        info = Task.objects.filter(status=4).count()
        for i in range(60):
            self.send(json.dumps({'value': info}))
            sleep(1)