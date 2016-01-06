from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.


class Sponsor(models.Model):
    image_model = models.ImageField(upload_to='photos/', blank=True ,default = 'photos/index.png')
    name = models.CharField(max_length=30, blank=True)
    info = models.TextField(blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Sponsor._meta.fields]
