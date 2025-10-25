from django.contrib.auth import get_user_model
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

User = get_user_model()

def send_admin_notification(
    message,
) : 
    layer = get_channel_layer()

    for user in User.objects.filter(is_superuser=True) : 
        async_to_sync(layer.group_send)(
            f'notification_layer_{user.id}',
            {
                'type': 'notify',
                'message': message
            }
        )

    return True