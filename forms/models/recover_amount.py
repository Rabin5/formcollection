from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models.contractor import Contractor


class RecoverAmount(FormBaseModel):
    pass


class RecoverAmountLine(FormLineBaseModel):
    contractor=models.ForeignKey(Contractor,on_delete=models.CASCADE,related_name='recover_amount_lines',verbose_name='ठेकेदारको नाम')
    income_name=models.CharField(max_length=500,verbose_name='आयको नाम')
    prev_year_rem_amt = models.FloatField(verbose_name='गत बर्षसम्मको बाँकी')
    this_year_recover_amt = models.FloatField(verbose_name='यस बर्षको बाँकी')
    cur_rem_amt = models.FloatField(verbose_name='बाँकी')
    rem_recover_amt = models.FloatField(verbose_name='यस बर्ष असुली')
    total_rem_amt = models.FloatField(verbose_name='जम्मा बाँकी')
    recover_amount = models.ForeignKey(
        RecoverAmount, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
