from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models import FiscalYear, ProcurementMethod
from master_data.models.government import GovernmentBody


class ReliefProcurementDetail(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, related_name='relief_body', verbose_name='निकायको नामः: ')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='relief_fiscal_year', verbose_name='आर्थिक बर्ष: ')

    def __str__(self):
        return self.body.name


class ReliefProcurementDetailLine(FormLineBaseModel):
    procure_method = models.ForeignKey(
        ProcurementMethod, on_delete=models.CASCADE, related_name='case_investigation_body', verbose_name='राहात सामग्री खरिद गर्दा प्रयोग गरेको विधि: ')
    amt_purchase = models.FloatField(verbose_name='खरिद रकम')
    reason_procure_method = models.CharField(
        max_length=300, verbose_name='उक्त खरिद विधि प्रयोग गर्नाको कारण')
    reliefprocurementdetail_line = models.ForeignKey(
        ReliefProcurementDetail, on_delete=models.CASCADE)
