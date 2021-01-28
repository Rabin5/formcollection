from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES
from master_data.models import FiscalYear, GovernmentBody, ProcurementMethod


class WardReliefProcureDistribution(FormBaseModel):

    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT,
                                    related_name='ward_relief', null=True, verbose_name='आर्थिक बर्ष: ')
    body = models.ForeignKey(GovernmentBody, on_delete=models.PROTECT,
                             related_name="ward_relief", null=True, verbose_name='निकायको नामः')
    state = models.CharField(
        max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return self.body.name


class WardReliefProcureDistributionLine(FormLineBaseModel):
    ward_relief = models.ForeignKey(
        WardReliefProcureDistribution, on_delete=models.CASCADE, related_name='lines')
    ward_num = models.IntegerField(verbose_name='वडा नं')

    amt_relief_material_purchase = models.FloatField(
        verbose_name="राहत सामग्री खरिद रकम")
    procure_method = models.ForeignKey(
        ProcurementMethod, on_delete=models.CASCADE, related_name='ward_relief_line', verbose_name="खरिद विधि")
    relief_beneficiary_family = models.CharField(
        max_length=500, verbose_name="राहत लाभग्राही परिवार")
    num_relief_benefitted = models.IntegerField(
        verbose_name='उपलव्ध गराएको राहतबाट सुविधा प्राप्त जनसंख्या')
    remarks = models.CharField(
        max_length=100, verbose_name='केही व्यहोरा भए खुलाउने ')

    def __str__(self):
        return self.procure_method.name
