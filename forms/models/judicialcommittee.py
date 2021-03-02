from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models.complaint_type import ComplaintType


class JudicialCommittee(FormBaseModel):
    pass


class JudicialCommitteeLine(FormLineBaseModel):
    judicialcommittee_line = models.ForeignKey(
        JudicialCommittee, on_delete=models.CASCADE, related_name='lines')
    complaint_type = models.ForeignKey(
        ComplaintType, on_delete=models.CASCADE, verbose_name='उजुरीको प्रकार')
    prev_remaining = models.FloatField(verbose_name='गतवर्षको बाँकी')
    current_addition = models.FloatField(verbose_name='यसवर्ष थप')
    total = models.FloatField(verbose_name='जम्मा')
    summed_up = models.FloatField(verbose_name='यो वर्ष फछर्यौट')
    remaining = models.FloatField(verbose_name='फछर्यौट हुन बाँकी')
    desc = models.CharField(
        max_length=300, verbose_name='समयमै फछर्यौट नहुनुको कारण')

    def __str__(self):
        return str(self.complaint_type.name)
