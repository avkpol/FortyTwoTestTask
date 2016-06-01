from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from PIL import Image as Img
import StringIO

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

'''
ticket #13
'''
STATUS_CHOICES = (
    (1, 'Standard'),
    (2, 'Higher'),
 )

class RequestLog (models.Model):

    datetime = models.CharField(max_length=40)
    requested_url = models.CharField(max_length=255)
    request_type = models.CharField(max_length=10, )
    request_ip = models.CharField(max_length=20)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1) #ticket #13

    def __unicode__(self):
        return '%s%s' %(self.requested_url, self.datetime)

    class Meta:
        app_label = 'avkpol4'


class ModelLog(models.Model):

    model = models.CharField(max_length=30)
    action = models.CharField(max_length=16)
    updated = models.DateTimeField(max_length=19, auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return "entry in {} {}d at {}".format(self.model, self.action, self.updated)

'''
signals
'''

models = ['UserData', 'RequestLog']
@receiver(post_save, sender= None)
def model_edit_save(sender, created, **kwargs):
    if sender.__name__ in models:
        if created:
            ModelLog.objects.create(model=sender.__name__, action='create')

        else:
            ModelLog.objects.create(model=sender.__name__, action='update')


@receiver(post_delete, sender= None)
def model_delete(sender, **kwargs):
    if sender.__name__ in models:
         ModelLog.objects.create(model=sender.__name__, action='delete')
