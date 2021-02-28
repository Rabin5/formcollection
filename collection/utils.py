import copy
from functools import reduce

from django.db.models.query import QuerySet
from django.db.models import Q
from django.urls.base import reverse

import django_filters


BS_MONTHS = [
    (1, "वैशाख"),
    (2, "जेष्ठ"),
    (3, "असार"),
    (4, "श्रावण"),
    (5, "भदौ"),
    (6, "आश्विन"),
    (7, "कार्तिक"),
    (8, "मंसिर"),
    (9, "पौष"),
    (10, "माघ"),
    (11, "फाल्गुण"),
    (12, "चैत्र"),
]

DEVANAGARI_DIGITS = (
    "०",
    "१",
    "२",
    "३",
    "४",
    "५",
    "६",
    "७",
    "८",
    "९"
)

STATES = [
    ('draft', 'Draft'),
    ('submitted', 'Submitted'),
]

STATUS = [
    ('started', 'STARTED'),
    ('incomplete', 'INCOMPLETE'),
    ('completed', 'COMPLETED'),
    ('submitted', 'SUBMITTED'),
    ('approved', 'APPROVED'),
    ('rejected', 'REJECTED'),
]

CH_STATE = [
    (0, 'fund_receipt_expense'),
    (1, 'risk_allowance'),
    (2, 'medical_expense'),
    (3, 'medical_receipt'),
    (4, 'medical_use'),
    (5, 'med_purchase_desc'),
    (6, 'pcr_test_compliance_detail'),
    (7, 'pcr_lab_detail'),
    (8, 'rdt_test_detail'),
    (9, 'pcr_kit_usage'),
    (10, 'covid_hos_mainpower'),
    (11, 'cov_hos_equipment'),
    (12, 'covid_hospital_detail'),
    (13, 'quarantine_management_detail'),
    (14, 'isolation_management_detail'),
    (15, 'quarantine_contruction_expenditure'),
    (16, 'isolation_construction_expenditure'),
    (17, 'cov_hos_management_checklist'),
]

PROVINCE_STATE = [
    (0, 'epidemic_outbreak_prep'),
    (1, 'fund_receipt_expense'),
    (2, 'risk_allowance'),
    (3, 'medical_expense'),
    (4, 'medical_receipt'),
    (5, 'medical_use'),
    (6, 'med_purchase_desc'),
    (7, 'pcr_test_compliance_detail'),
    (8, 'pcr_lab_detail'),
    (9, 'rdt_test_detail'),
    (10, 'pcr_kit_usage'),
    (11, 'covid_hos_mainpower'),
    (12, 'cov_hos_equipment'),
    (13, 'covid_hospital_detail'),
    (14, 'quarantine_management_detail'),
    (15, 'isolation_management_detail'),
    (16, 'quarantine_contruction_expenditure'),
    (17, 'isolation_construction_expenditure'),
    (18, 'district_covid_management'),
    (19, 'fund_operation'),
]

INTERNAL_AFFAIRS_STATE = [
    (0, 'epidemic_outbreak_prep'),
    (1, 'fund_receipt_expense'),
    (2, 'risk_allowance'),
    (3, 'action_plan_implementation'),
]

CHIEF_MINISTER_STATE = [
    (0, 'epidemic_outbreak_prep'),
    (1, 'fund_receipt_expense'),
    (2, 'risk_allowance'),
    (3, 'province_institute_management'),
    (4, 'action_plan_implementation'),
]

LOCAL_LEVEL_STATE = [
    (0, 'epidemic_outbreak_prep'),
    (1, 'fund_receipt_expense'),
    (2, 'risk_allowance'),
    (3, 'medical_expense'),
    (4, 'medical_receipt'),
    (5, 'medical_use'),
    (6, 'med_purchase_desc'),
    (7, 'case_investigation_tracing'),
    (8, 'covid_hos_mainpower'),
    (9, 'cov_hos_equipment'),
    (10, 'quarantine_management_detail'),
    (11, 'isolation_management_detail'),
    (12, 'quarantine_contruction_expenditure'),
    (13, 'isolation_construction_expenditure'),
    (14, 'case_investigation_tracing_operation'),
    (15, 'relief_procurement_detail'),
    (16, 'relief_procurement_distribution'),
    (17, 'ward_relief_procurement_dist'),
    (18, 'received_relief_detail'),
    (19, 'relief_distribution_expense'),
    (20, 'action_plan_implementation')
]


def num_to_devanagari(num):
    """
    Utility function to convert an integer number to Devanagari
    """
    dev_num = ''
    if type(num) != int:
        return -1

    for digit in str(num):
        dev_num += DEVANAGARI_DIGITS[int(digit)]

    return dev_num


def find_empty_fields(object, app_name, url_name, ROUTE_LINK, STATE):
    """
    find all the empty field in collection and
    return form number, form title and url.
    to show warning message to user before they submit a collection.
    """
    update_url = app_name + ":" + url_name
    payload = []
    updated_ch_state = copy.deepcopy(STATE)
    for field in STATE:
        if field[1] == "district_covid_management":
            district_covid_mgmt_lines_exists = (
                len(getattr(object, field[1]).dist_quarantine_lines.all()) == 0
                and len(
                    getattr(object, field[1]).dist_isolation_lines.all()
                ) == 0
                and len(getattr(object, field[1]).dist_lab_lines.all()) == 0
            )
            if district_covid_mgmt_lines_exists:
                is_empty = True
            else:
                is_empty = False
        else:
            is_empty = len(getattr(object, field[1]).lines.all()) == 0

        if not is_empty:
            updated_ch_state.remove(field)

    for val in updated_ch_state:
        if val[1] in ROUTE_LINK:
            payload.append(
                {
                    "order_no": val[0] + 1,
                    "title": ROUTE_LINK[val[1]]["title"],
                    "url": reverse(update_url, kwargs={"pk": object.pk})
                    + f"?form={val[1]}",
                }
            )

    return payload




def __remove_none_fields(fields: dict) -> dict:
    '''
        Returns:
            {'province': '1', 'district': '2'}
    '''
    return {k: v for k, v in fields.items() if v is not None and v }

def filter_helper(objects: QuerySet, fields: dict=None):
    query_list = __remove_none_fields(fields)
    
    objects = objects.filter(
        Q(**query_list)
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