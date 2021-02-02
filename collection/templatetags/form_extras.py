from django import template
from django.db.models import Sum
from collection.models import ProvinceFormCollection
from collection.utils import num_to_devanagari

register = template.Library()


@register.filter(name="num_to_devanagari_temp")
def num_to_devanagari_temp(value):
    """
    returns devanagari value if used in template tag
    """
    return num_to_devanagari(value)


@register.simple_tag
def calculate_percentage(numerator, denominator):
    percentage = numerator / denominator * 100
    return round(percentage, 2)


@register.simple_tag
def calculate_total_province(value, otm_field_name, rel_name, field_to_total):
    sum_query = otm_field_name + "__" + rel_name + "__" + field_to_total
    total = (
        ProvinceFormCollection.objects.filter(id=value.id)
        .aggregate(Sum(sum_query))
        .get(f"{sum_query}__sum")
    )
    return total
