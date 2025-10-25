from .models import Product
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .utlities import send_admin_notification


@receiver(post_save, sender=Product)
def product_created(sender, instance, created, **kwargs):
    
    if not created:
        return
    
    send_admin_notification(f"Product '{instance.title}' has been created.")


@receiver(post_delete, sender=Product)
def product_deleted(sender, instance, **kwargs):
    send_admin_notification(f"Product '{instance.title}' has been deleted.")