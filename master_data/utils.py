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

def filter_helper(objects: QuerySet, query: str=None, fields: list=None):
    query = query.strip()
    query_list = __search_query(query, fields)
    # Similar to  objects.filter(Q(name__icontains=query), Q(type__icontains=query))
    objects = objects.filter(
        reduce(operator.or_,
        (Q(**query_dict) for query_dict in query_list))
    )
    return objects

