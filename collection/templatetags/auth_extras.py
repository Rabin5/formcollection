from django import template
from django.contrib.auth.models import Group 

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_names):
    group_names = group_names.split(", ")
    for group_name in group_names:
        group = Group.objects.get(name=group_name)
        if group in user.groups.all():
            return True 
    return False