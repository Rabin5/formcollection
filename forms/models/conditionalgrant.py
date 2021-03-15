from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.grant_type import GrantType


class ConditionalGrant(FormBaseModel):
    pass


class ConditionalGrantLine(FormLineBaseModel):
    condtionalgrant_line = models.ForeignKey(
        ConditionalGrant, on_delete=models.CASCADE, related_name='lines')
    grant_type = models.ForeignKey(
        GrantType, on_delete=models.CASCADE, verbose_name='अनुदानको किसिम')
    total_grant = models.IntegerField(verbose_name='जम्मा अनुदान')
    expense = models.FloatField(verbose_name='खर्च')
    freeze_amount = models.FloatField(verbose_name='बाँकि (फ्रिज हुनुपर्नें)')
    remarks = models.CharField(max_length=300, verbose_name='कैफियत')

    def __str__(self):
        return str(self.grant_type)
