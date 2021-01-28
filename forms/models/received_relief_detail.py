from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES
from master_data.models import FiscalYear, GovernmentBody, Institution, UnitOfMeasure,Product


class ReceivedReliefDetail(FormBaseModel):

    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT,
                                    related_name='receivedrelief', null=True, verbose_name='आर्थिक बर्ष:')
    body = models.ForeignKey(GovernmentBody, on_delete=models.PROTECT,
                             related_name="receivedrelief", null=True, verbose_name='निकायको नामः')
    state = models.CharField(
        max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return self.body.name


class ReceivedReliefDetailLine(FormLineBaseModel):
    ward_relief = models.ForeignKey(
        ReceivedReliefDetail, on_delete=models.CASCADE, related_name='lines')
    provider = models.ForeignKey(
        Institution, on_delete=models.CASCADE, related_name='receivedrelief', verbose_name='राहत सामग्री प्रदान गर्नेको नाम')
    unit = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE,
                             related_name='receivedrelief', verbose_name='ईकाइ')
    qty_received = models.FloatField(
        verbose_name="प्राप्त परिमाण")
    qty_distributed = models.FloatField(verbose_name="वितरण परिमाण")
    relief_material = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='received_relief_line', verbose_name="राहत सामग्री")
    qty_remaining = models.FloatField(verbose_name="बाँकी परिमाण ")

    def __str__(self):
        return self.provider.name
