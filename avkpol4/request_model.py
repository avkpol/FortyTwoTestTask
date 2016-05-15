from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class RequestLog (models.Model):
    datetime = models.CharField(max_length=25)
    requested_url = models.CharField(max_length=255)
    request_type = models.CharField(max_length=10)
    request_ip = models.CharField(max_length=20)

    def __str__(self):
        return '%s%s' %(self.requested_url, self.datetime)


@receiver(post_save, sender = RequestLog)
def new_notification(sender, **kwargs):
    if kwargs.get('created', True):
        print "new request sent!"




