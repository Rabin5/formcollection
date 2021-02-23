from functools import reduce
import operator

from django.db.models.query import QuerySet
from django.db.models import Q
import django_filters

def __search_query(query: str, fields: list) -> list:
    '''
        Returns:
            [{'name': val}, {'type': val}]
    '''
    return [{field: query} for field in fields]

def filter_helper(objects: QuerySet, query: str, fields: list, foreign_fields: list=None):
    query = query.strip()
    query_list = __search_query(query, fields)
    # Similar to  objects.filter(Q(name__icontains=query), Q(type__icontains=query))
    objects = objects.filter(
        reduce(operator.or_,
        (Q(**query_dict) for query_dict in query_list))
    )
    return objects



class ReportFilter(django_filters.FilterSet):
    """ Filter Report a/c to created_at field using django-filters package"""
    start_date = django_filters.DateFilter(
        field_name='created_at', lookup_expr='date__gte')
    end_date = django_filters.DateFilter(
        field_name='created_at', lookup_expr='date__lte')

    class Meta:
        # model = Report
        fields = []
