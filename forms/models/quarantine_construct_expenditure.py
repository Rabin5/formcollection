from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES
from master_data.models import FiscalYear, GovernmentBody, Product, UnitOfMeasure, ProcurementMethod


class QuarantineConstructionExpenditure(FormBaseModel):
    """
    Model for form class: 1_covid_hospital/16.puml
    Code: medExp
    """
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, related_name='forms_quarantine_expense_fy', null=True)
    body = models.ForeignKey(GovernmentBody, on_delete=models.CASCADE, related_name="forms_quarantine_expense_gov", null=True)
    state = models.CharField(max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return f'{self.fiscal_year}'


class QuarantineConstructionExpenditureLine(FormLineBaseModel):
    quarantine_construction = models.ForeignKey(QuarantineConstructionExpenditure, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='quarantine_product', verbose_name='खरिद भएका सामग्री')
    uom = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE, related_name='quarantine_uom', verbose_name='इकाई')
    number = models.FloatField( verbose_name='संख्या')
    unit_cost = models.FloatField(verbose_name='प्रति ईकाइ दर')
    amt_expense = models.FloatField(verbose_name='खर्च रकम')
    procure_method = models.ForeignKey(ProcurementMethod, on_delete=models.CASCADE, related_name='quarantine_procure', verbose_name='खरिद विधि')
    remarks = models.CharField(max_length=50, blank=True, null=True, verbose_name='कैफियत')

    