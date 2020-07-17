from django.db.models import signals, Count
from django.dispatch import receiver
from django.conf import settings


# pre_save method signal
from fcm_django.models import FCMDevice
from pyfcm import FCMNotification

from .models import Sm, CustomFCMDevice, Device


@receiver(signals.pre_save, sender=Sm)
def check_product_description(sender, instance, **kwargs):
    if not instance.mobilenumber:
        instance.mobilenumber = '09053635521'


# post_save method
#@receiver(signals.post_save, sender=Sm)
#def create_product(sender, instance, created, **kwargs):
#    devices = Device.objects.values('device_id').annotate(dcount=Count('device_id'))
#    for device in devices:
#        push_service = FCMNotification(api_key=settings.FCM_DJANGO_SETTINGS["FCM_SERVER_KEY"])
#       registration_id = device['device_id']
#        message_title = instance.message
#        message_body = instance.id
#        result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
#                                                   message_body=message_body)
#        print
#        result