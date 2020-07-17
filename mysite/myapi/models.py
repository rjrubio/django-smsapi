from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from fcm_django.models import AbstractFCMDevice


class Sm(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    mobilenumber = models.CharField(max_length=15)
    message = models.CharField(max_length=512)
    status = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.mobilenumber


class Device(models.Model):
    device_id = models.CharField(max_length=512, null=False, blank=False)
    device_model = models.CharField(max_length=128)
    device_manufacturer = models.CharField(max_length=128)
    status = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.device_model


class College(models.Model):
    college_name = models.CharField(max_length=60, null=True, blank=True)
    status = models.IntegerField()
    created_at = models.CharField(max_length=160)

    def __str__(self):
        return self.college_name


class Meta(models.Model):
    timestamp = models.CharField(max_length=60, null=True, blank=True)
    client_id = models.CharField(max_length=160)

    def __str__(self):
        return self.timestamp


class CustomFCMDevice(AbstractFCMDevice):
    language = models.CharField(max_length=35, blank=False)
    position = models.CharField(max_length=35, blank=False)
    app_version = models.CharField(max_length=35, blank=False)


@receiver(signals.post_save, sender=Sm)
def create_product(sender, instance, created, **kwargs):
    print("Save method is called")
