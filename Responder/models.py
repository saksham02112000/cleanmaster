from django.db import models

OPEN_CLOSE_CHOICES = (('close', 'close'), ('open', 'open'))


class DevicePings(models.Model):
    client_id = models.CharField(max_length=1024)
    dist_reading = models.CharField(max_length=1024, blank=True, null=True)
    mq2reading = models.CharField(max_length=1024, blank=True, null=True)
    mq3reading = models.CharField(max_length=1024, blank=True, null=True)
    mq4reading = models.CharField(max_length=1024, blank=True, null=True)


class DeviseResponse(models.Model):
    client_id = models.CharField(max_length=1024)
    next_response = models.CharField(max_length=1024, default='close')


# Create your models here.
