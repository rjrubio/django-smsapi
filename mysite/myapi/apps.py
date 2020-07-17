from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class MyapiConfig(AppConfig):
    name = 'myapi'

    def ready(self):
        from .signals import signals  # noqa