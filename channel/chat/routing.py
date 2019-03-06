from django.urls import path

from .consumers import ChatConsumer

_urlpatterns = [
    path('ws/chat/<int:room_name>/', ChatConsumer),
]