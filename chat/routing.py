from django.urls import path
from .consumers import ChatWebsocketConsumer

websocket_urlpatterns = [
    path("chat/<str:room_slug>/", ChatWebsocketConsumer.as_asgi()),
]
