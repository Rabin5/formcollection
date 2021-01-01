from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, GovernmentBody, OfficeBearer, AllowanceType


class RiskAllowance(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नामः: ')
    fiscal_year_from = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='forms_fre_fy_from', verbose_name='आर्थिक बर्ष: ')

    def __str__(self):
        return self.fiscal_year_from


class RiskAllowanceLine(FormLineBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='खर्च गर्ने निकायको नाम')
    office_bearer = models.ForeignKey(
        OfficeBearer, on_delete=models.PROTECT, verbose_name='जोखिम भत्ता पाउने पदाधिकारी')
    bearer_num = models.IntegerField(
        verbose_name='कर्मचारी वा पदाधिकारी संख्या')
    allowance_type = models.ForeignKey(
        AllowanceType, on_delete=models.PROTECT, verbose_name='भत्ताको प्रकार')
    expense_amount = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name='सम्म खर्च रकम')
    remarks = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name='कैफियत')
    risk_allowance_line = models.ForeignKey(
        RiskAllowance, on_delete=models.PROTECT)

    def __str__(self):
        return self.body
