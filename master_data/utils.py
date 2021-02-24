from functools import reduce
import operator

from django.db.models.query import QuerySet
from django.db.models import Q
import django_filters

def __search_query(query: str, fields: list) -> list:
    '''
        Returns:
            [{'name__icontains': val}, {'type__icontains': val}]
    '''
    return [{f'{field}__icontains': query} for field in fields]

def filter_helper(objects: QuerySet, query: str=None, fields: list=None, address: bool=False):
    query = query.strip()
    query_list = __search_query(query, fields)
    # Similar to  objects.filter(Q(name__icontains=query), Q(type__icontains=query))
    objects = objects.filter(
        reduce(operator.or_,
        (Q(**query_dict) for query_dict in query_list))
    )
    return objects


def date_filter(model_class, field_name):
    class ModelDateFilter(django_filters.FilterSet):
        """ Filter respective field using django-filters package"""
        start_date = django_filters.DateFilter(
            field_name=field_name, lookup_expr='date__gte')
        end_date = django_filters.DateFilter(
            field_name=field_name, lookup_expr='date__lte')

        class Meta:
            model = model_class
            fields = []
    return ModelDateFilter
