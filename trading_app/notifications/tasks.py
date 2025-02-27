from celery import shared_task
from django.contrib.auth import get_user_model
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification

User = get_user_model()

@shared_task
def send_notification(user_id, notification_type, message):
    user = User.objects.get(id=user_id)

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"notifications_{user.id}", {"type": "send_notification", "message": message}
    )
