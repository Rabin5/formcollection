from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, SubHeader, WorkNature
from master_data.models.government import GovernmentBody


class ProcurementAuditor(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नाम')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, verbose_name='आर्थिक बर्ष')

    def __str__(self):
        return self.body.name


class ProcurementAuditorLine(FormLineBaseModel):
    sub_header = models.ForeignKey(
        SubHeader, on_delete=models.PROTECT, verbose_name='उपशीर्षकको नाम')
    work_nature = models.ForeignKey(
        WorkNature, on_delete=models.PROTECT, verbose_name='कामको प्रकृति')
    amt_expense_estimate = models.FloatField(verbose_name='लागत अनुमान')
    num_piece = models.FloatField(verbose_name='टुक्रा संख्या')
    amt_expense = models.FloatField(verbose_name='खर्च रकम')
    procurement_auditor_line = models.ForeignKey(
        ProcurementAuditor, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
