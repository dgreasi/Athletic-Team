import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

#Announcements
class Announcement(models.Model):
    #Text to be announced
    announcement_text = models.TextField()
    #Date of publication
    pub_date = models.DateTimeField('date published')

    #Display recent annoucements and not future
    #create better form of object in base
    def __str__(self):              # __unicode__ on Python 2
        return self.announcement_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

#comments to Announcements
class Comment(models.Model):
    #comments is foreignKey to announcement
    announcement = models.ForeignKey(Announcement)
    #field of comment
    comment_text = models.TextField()
    #field of vote
    votes = models.IntegerField(default=0)
    #create better form of object in base
    def __str__(self):              # __unicode__ on Python 2
        return self.comment_text


