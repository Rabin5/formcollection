from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS


class RevenueDistribution(FormBaseModel):
    pass


class RevenueDistributionLine(FormLineBaseModel):
    title= models.CharField(max_length=300, blank=True, null=True, verbose_name='आय शीर्षक')
    collected_amount = models.FloatField(verbose_name='संकलित रकम')
    percentage_sent_state = models.FloatField(verbose_name='प्रदेशलाई पठाउनु पर्ने प्रतिशत')
    sent_amount = models.FloatField(verbose_name='पठाएको रकम')
    remaining_amount = models.FloatField(blank=True, null=True, verbose_name='पठाउन बाँकी रकम')
    revenue_distribution = models.ForeignKey(
         RevenueDistribution, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
