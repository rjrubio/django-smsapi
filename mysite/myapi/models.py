from django.db import models


class Sm(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    mobilenumber = models.CharField(max_length=15)
    message = models.CharField(max_length=160)
    status = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.mobilenumber


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

