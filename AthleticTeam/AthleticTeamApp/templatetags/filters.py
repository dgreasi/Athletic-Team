from django import template 
from django.contrib.auth.models import Group

#coach staff
register = template.Library() 

@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False

@register.filter(name='str_equal')
def str_equal(str1, str2): 
    if str1 == str2 :
    	return True
    else:
    	return False
