from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.convenience_type import ConvenienceType
from collection.utils import STATES


class AdditionalConvenience(FormBaseModel):
    pass


class AdditionalConvenienceLine(FormLineBaseModel):
    additionalconvenction_line = models.ForeignKey(
        AdditionalConvenience, on_delete=models.CASCADE, related_name='lines')
    convenience_type = models.ForeignKey(
        ConvenienceType, on_delete=models.CASCADE, related_name='lines', verbose_name='सुविधाको किसिम')
    conveniece_staff_count = models.IntegerField(
        verbose_name='सुविधा उपयोगको संख्या कर्मचारी')
    convenience_officer_count = models.IntegerField(
        verbose_name='सुविधा उपयोगको संख्या पदाधिकारी')
    yearly_expense = models.FloatField(verbose_name='बार्षिक खर्च')
    remarks = models.CharField(max_length=300, verbose_name='कैफियत')

    def __str__(self):
        return self.conveniece_staff_count
