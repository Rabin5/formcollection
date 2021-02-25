from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import GovernmentBody,GrantType, grant_type



class  ExpenditureDetail(FormBaseModel):
    pass


class  ExpenditureDetailLine(FormLineBaseModel):
    grant_providing_body=models.ForeignKey(GovernmentBody,verbose_name='अनुदान प्रदान गर्ने निकाय',on_delete=models.PROTECT,related_name='expenditure_detail_line')
    grant_type=models.ForeignKey(GrantType,verbose_name='अनुदानको प्रकार',on_delete=models.PROTECT,related_name='expenditure_detail_lines')
    received_amount = models.FloatField(verbose_name='प्राप्त रकम')
    expensed_amount = models.FloatField(verbose_name='खर्च रकम')
    remaining_amount = models.FloatField(verbose_name='बाँकी रकम')
    expenditure_detail = models.ForeignKey(
         ExpenditureDetail, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')