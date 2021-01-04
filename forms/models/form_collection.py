from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, GovernmentBody

class FormCollection(models.Model):
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, related_name='forms_medExp_fy')
    body = models.ForeignKey(GovernmentBody, on_delete=models.CASCADE, related_name="forms_medExp_gov")

    def __str__(self) -> str:
        return f'{self.fiscal_year}'