from django.db import models


class Sm(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    mobilenumber = models.CharField(max_length=15)
    message = models.CharField(max_length=160)
    status = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.mobilenumber