from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models.contractor import Contractor


class ContractDesc(FormBaseModel):
    pass


class ContractDescLine(FormLineBaseModel):
    contractor_name=models.ForeignKey(Contractor,on_delete=models.CASCADE,related_name='contractor_desc_lines',verbose_name='ठेकेदारको नाम')
    description = models.CharField(max_length=300,blank=True, null=True, verbose_name='ठेक्काको विवरण')
    agreement_date = models.DateField(verbose_name='सम्झौता मिति')
    contract_duration = models.PositiveIntegerField(verbose_name='ठेक्का अवधि')
    contract_amount = models.FloatField(verbose_name='ठेक्का रकम')
    recover_amount = models.FloatField(verbose_name='असुली रकम')
    remaining_recover_amount = models.FloatField(verbose_name='असुल हुन बाँकी')
    remarks = models.CharField(max_length=500,blank=True, null=True, verbose_name='कैफियत')
    contract_desc = models.ForeignKey(
        ContractDesc, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
    
