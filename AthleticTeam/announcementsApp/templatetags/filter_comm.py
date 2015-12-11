from django import template
from announcementsApp.models import Comment, Announcement

register = template.Library() 
#check if this user has made a comment in this announcement
#register.filter('has_comment', has_comment)

@register.filter(name='has_comment')
def has_comment(user, list_comments): 
    if any(comment.owner == user for comment in list_comments):
    	return True
    else:
    	return False
