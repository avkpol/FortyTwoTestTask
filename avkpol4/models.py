from django.db import models

class User_data(models.Model):
    name = models.CharField(max_length=125, verbose_name= "Name")
    last_name = models.CharField(max_length=125, verbose_name= "Last name")
    birth_date = models.DateField( verbose_name="Date of Birth", null=True)
    bio = models.TextField( verbose_name="Bio")
    email = models.EmailField(verbose_name="Email")
    jabber = models.EmailField(verbose_name="Jabber")
    skype = models.CharField(max_length=125, verbose_name="Skype")

    def __str__(self):
        return '%s' %(self.last_name)



