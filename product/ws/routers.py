from .consumers import NotificationConsumer
from django.urls import path

urlpatterns = [
    path('ws/notifications', NotificationConsumer.as_asgi()),
]