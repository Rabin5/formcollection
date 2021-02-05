from collection.models import (CovHosFormCollection,
                               InternalAffairFormCollection,
                               ProvinceFormCollection,
                               ChiefMinisterOfficeFormCollection,
                               LocalLevelFormCollection)
from collection.utils import num_to_devanagari
from django import template
from django.db.models import Sum

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
def calculate_total_covid_hospital(value, otm_field_name, rel_name, field_to_total):
    sum_query = otm_field_name + "__" + rel_name + "__" + field_to_total
    total = (
        CovHosFormCollection.objects.filter(id=value.id)
        .aggregate(Sum(sum_query))
        .get(f"{sum_query}__sum")
    )
    return total

@register.simple_tag
def calculate_total_province(value, otm_field_name, rel_name, field_to_total):
    sum_query = otm_field_name + "__" + rel_name + "__" + field_to_total
    total = (
        ProvinceFormCollection.objects.filter(id=value.id)
        .aggregate(Sum(sum_query))
        .get(f"{sum_query}__sum")
    )
    return total

@register.simple_tag
def calculate_total_internal_affair(value, otm_field_name, rel_name, field_to_total):
    sum_query = otm_field_name + "__" + rel_name + "__" + field_to_total
    total = (
        InternalAffairFormCollection.objects.filter(id=value.id)
        .aggregate(Sum(sum_query))
        .get(f"{sum_query}__sum")
    )
    return total

@register.simple_tag
def calculate_total_chief_minister(value, otm_field_name, rel_name, field_to_total):
    sum_query = otm_field_name + "__" + rel_name + "__" + field_to_total
    total = (
        ChiefMinisterOfficeFormCollection.objects.filter(id=value.id)
        .aggregate(Sum(sum_query))
        .get(f"{sum_query}__sum")
    )
    return total

@register.simple_tag
def calculate_total_local_level(value, otm_field_name, rel_name, field_to_total):
    sum_query = otm_field_name + "__" + rel_name + "__" + field_to_total
    total = (
        LocalLevelFormCollection.objects.filter(id=value.id)
        .aggregate(Sum(sum_query))
        .get(f"{sum_query}__sum")
    )
    return total