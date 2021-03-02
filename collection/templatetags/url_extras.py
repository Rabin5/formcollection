from django import template


register = template.Library()

@register.filter(name='url_contains')
def url_contains(url_list, view_name):
    for url in url_list.split(', '):
        if url in view_name:
            return True
    return False