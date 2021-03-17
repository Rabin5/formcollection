from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import ConstructionCompany
from master_data.models.government import GovernmentBody
from master_data.models.fiscal_year import FiscalYear


class SubsistenceAllowance(FormBaseModel):
    pass


class SubsistenceAllowanceLine(FormLineBaseModel):
    subsistenceallowance_line = models.ForeignKey(
        SubsistenceAllowance, on_delete=models.CASCADE, null=True, blank=True, related_name='lines')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.CASCADE, verbose_name='आर्थिक वर्ष')

    total_unemployed_families = models.IntegerField(
        verbose_name='वेरोजगार परिवारला')
    subsistence_allowance_amount = models.FloatField(
        verbose_name='निर्वाह भत्ता वितरण रु.')

    def __str__(self):
        return self.total_unemployed_families
