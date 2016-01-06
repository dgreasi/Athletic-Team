from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.


class Administration(models.Model):

    PRE = 'President'
    MEM = 'Member'
    EXD = 'Executive Director'
    TED = 'Technical Director'
    FMO = 'Football Manager Operation Department'
    CEO = 'CEO'
    COD = 'Communications Director'
    CDI = 'Commercial Director'
    DGM = 'Deputy General Manager-Communication and Public Relations'
    CFO ='CFO'
    
    # model fields
    available_positions = (
                            (PRE,'President'),
                            (MEM,'Member'),
                            (EXD,'Executive Director'),
                            (TED,'Technical Director'),
                            (FMO,'Football Manager Operation Department'),
                            (CEO,'CEO'),
                            (COD,'Communications Director'),
                            (CDI,'Commercial Director'),
                            (DGM,'Deputy General Manager-Communication and Public Relations'),
                            (CFO,'CFO'),
                        )

    image = models.ImageField(upload_to='photos/', blank=True ,default = 'photos/index.png')
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile = models.TextField(blank=True)
    position = models.CharField(max_length=50, choices=available_positions, blank=True)
    nationality =  models.CharField(max_length=30, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.last_name

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Administration._meta.fields]
