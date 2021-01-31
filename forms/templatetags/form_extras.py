from django import template
from forms.utils import num_to_devanagari

register = template.Library()


@register.filter(name="num_to_devanagari_temp")
def num_to_devanagari_temp(value):
    """
    returns devanagari value if used in template tag
    """
    return num_to_devanagari(value)