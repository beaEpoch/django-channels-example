from django.urls import path

from .consumers import ChatConsumer

_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatConsumer),
]