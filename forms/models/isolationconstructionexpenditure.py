from master_data.models import FiscalYear
from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.hospital import CovidHospital
from master_data.models.government import GovernmentBody, Manpower
from master_data.models.product import UnitOfMeasure, Product, ProcurementMethod


class IsolationConstructionExependiture(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, related_name='iso_centerexpentiture', verbose_name='निकायको नामः: ')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='iso_cenexpentiture_fiscal_year', verbose_name='आर्थिक बर्ष: ')

    def __str__(self):
        return self.body.name


class IsolationConstructionExependitureLine(FormLineBaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, verbose_name='खरिद भएका सामग्री')
    uom = models.ForeignKey(UnitOfMeasure, on_delete=models.PROTECT,
                            verbose_name='इकाई')
    number = models.FloatField(
        verbose_name='संख्या')
    unit_cost = models.FloatField(
        verbose_name='प्रति ईकाइ दर')
    amt_expense = models.FloatField(
        verbose_name='खर्च रकम')
    procure_method = models.ForeignKey(
        ProcurementMethod, on_delete=models.PROTECT, verbose_name='खरिद विधि')
    remarks = models.CharField(max_length=300, verbose_name='कैफियत')
    isolation_cons_expentiture_line = models.ForeignKey(
        IsolationConstructionExependiture, on_delete=models.PROTECT)
