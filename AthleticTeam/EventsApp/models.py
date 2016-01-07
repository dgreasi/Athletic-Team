from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
   # created = models.DateTimeField(auto_now_add=True)
    #modified = models.DateTimeField(auto_now=True)
   # owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    location = models.CharField(max_length=30)
    event_content = models.TextField( blank=True)
    attendee = models.ManyToManyField(User, blank=True)
    ACTIVATE = models.BooleanField(default=False)
    #objects = EventManager()


    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Event._meta.fields]


