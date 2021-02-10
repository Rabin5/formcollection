from django import template
from django.contrib.auth.models import Group 

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_names):
    group_names = group_names.split(", ")

    for group_name in group_names:
        if user.groups.filter(name__icontains=group_name).exists():
            return True
    return False