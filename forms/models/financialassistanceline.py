from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import ConstructionCompany
from master_data.models.government import GovernmentBody
from master_data.models.fiscal_year import FiscalYear


class FinancialAssistance(FormBaseModel):
    pass


class FinancialAssistanceLine(FormLineBaseModel):
    financialassistance_line = models.ForeignKey(
        FinancialAssistance, on_delete=models.CASCADE, null=True, blank=True, related_name='lines')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.CASCADE, verbose_name='आर्थिक वर्ष')

    foreign_employment_board_received_amount = models.FloatField(
        verbose_name='वैदेशिक रोजगार बोर्डबाट प्राप्त रु.')
    concerned_distribution_amount = models.FloatField(
        verbose_name='सम्बन्धीतलाइ वितरण रु.')

    def __str__(self):
        return self.foreign_employment_board_received_amount
