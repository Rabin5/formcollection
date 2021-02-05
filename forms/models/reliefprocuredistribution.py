from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models import FiscalYear
from master_data.models.government import GovernmentBody
from master_data.models.product import UnitOfMeasure, Product


class ReliefProcureDistribution(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, related_name='reliefprocuredistribution_body', verbose_name='निकायको नामः: ')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='reliefprocuredistribution_fiscal_year', verbose_name='आर्थिक बर्ष: ')

    def __str__(self):
        return self.body.name


class ReliefProcureDistributionLine(FormLineBaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='case_investigation_body', verbose_name='राहत सामग्री')
    uom = models.ForeignKey(
        UnitOfMeasure, on_delete=models.CASCADE, verbose_name='ईकाइ')
    qty_purchase = models.FloatField(
        blank=True, null=True, verbose_name='खरिद परिमाण ')
    rate = models.FloatField(
        blank=True, null=True, verbose_name='प्रतिईकाइ दर')
    amt_total = models.FloatField(
        blank=True, null=True, verbose_name='रकम')
    qty_distributed = models.FloatField(
        blank=True, null=True, verbose_name='वितरण परिमाण')
    qty_remaining = models.FloatField(
        blank=True, null=True, verbose_name='बाँकी परिमाण ')
    has_quality_complaint = models.BooleanField(
        verbose_name='गुणस्तरमा सिकायत छ । छैन')
    reliefprocuredistribution_line = models.ForeignKey(
        ReliefProcureDistribution, on_delete=models.CASCADE, related_name='lines')
