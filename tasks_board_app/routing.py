from django.urls import path
from .consumers import InfoConsumer

websocket_urlpatterns = [
    path('ws/info/', InfoConsumer.as_asgi()),
]
