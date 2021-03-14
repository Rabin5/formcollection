from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS



class TransparencyDetail(FormBaseModel):
    pass


class TransparencyDetailLine(FormLineBaseModel):
    details=models.TextField(verbose_name='विवरण')
    is_true = models.BooleanField(verbose_name='छ वा छैन')
    remarks = models.CharField(verbose_name='कैफियत', max_length=500, blank=True, null=True)
    
    transparency_detail_line = models.ForeignKey(
        TransparencyDetail, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
