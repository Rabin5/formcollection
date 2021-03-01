from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models.peski_bibaran import PeskiBibaran


class IntegralAdvancement(FormBaseModel):
    pass


class IntegralAdvancementLine(FormLineBaseModel):
    desc=models.TextField(verbose_name='विवरण')
    remaining_advance = models.FloatField(verbose_name='यस बर्ष फछ्यौंट')
    cancelled_amount= models.FloatField(verbose_name='गत बर्षको पेश्की बाँकी')
    remaining_amount = models.FloatField(verbose_name='गत बर्षको बाँकी')
    added_amount = models.FloatField(verbose_name='यस बर्षको थप')
    total = models.FloatField(verbose_name='जम्मा')
    integral_advancement= models.ForeignKey(
        IntegralAdvancement, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
    
