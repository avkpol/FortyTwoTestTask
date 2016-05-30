from django.db import models
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.signals import post_save
from django.dispatch import receiver

from PIL import Image as Img
import StringIO # Used to imitate reading from byte file


class UserData(models.Model):

    name = models.CharField(max_length=125, verbose_name= "Name")
    last_name = models.CharField(max_length=125, verbose_name= "Last name")
    birth_date = models.DateField( verbose_name="Date of Birth", null=True)
    bio = models.TextField(verbose_name="Bio")
    email = models.EmailField(verbose_name="Email")
    jabber = models.EmailField(verbose_name="Jabber")
    skype = models.CharField(max_length=125, verbose_name="Skype")
    photo = models.ImageField(upload_to = 'photo/', blank=True, null=True)

    class Meta:
        app_label = 'avkpol4'

    def get_absolute_url(self):
        return reverse("user_edit", kwargs={"pk": self.id, 'photo':self.photo})

    def save(self, *args, **kwargs):
            if self.photo:
                image = Img.open(StringIO.StringIO(self.photo.read()))
                image.thumbnail((200, 200), Img.ANTIALIAS)
                output = StringIO.StringIO()
                image.save(output, format='JPEG', quality=75)
                output.seek(0)
                self.photo = InMemoryUploadedFile(output, 'ImageField',
                                                  self.photo.name, 'image/jpeg',
                                                  output.len, None)
            # replace image instead
            try:
                current = UserData.objects.get(id=self.id)
                if current.photo != self.photo:
                    current.photo.delete(save=False)
            except:
                pass

            super(UserData, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.last_name

class RequestLog (models.Model):
    datetime = models.CharField(max_length=25)
    requested_url = models.CharField(max_length=255)
    request_type = models.CharField(max_length=10)
    request_ip = models.CharField(max_length=20)

    def __unicode__(self):
        return '%s%s' %(self.requested_url, self.datetime)

    class Meta:
        app_label = 'avkpol4'

@receiver(post_save, sender = RequestLog)
def new_notification(sender, **kwargs):
    if kwargs.get('created', True):
        print "new request sent!"
