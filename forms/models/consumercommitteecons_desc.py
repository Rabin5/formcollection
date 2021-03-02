from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models.complaint_type import ComplaintType


class ConsumerCommitteeConstructionDescription(FormBaseModel):
    pass


class ConsumerCommitteeConstructionDescriptionLine(FormLineBaseModel):
    consumercommitteeconstructiondescription_line = models.ForeignKey(
        ConsumerCommitteeConstructionDescription, on_delete=models.CASCADE, related_name='lines')
    program = models.TextField(verbose_name='कार्यक्रमको नाम')
    total_expense = models.FloatField(
        verbose_name='निर्माण कार्यमा भएको कुल खर्च')
    consumer_committee_expense = models.FloatField(
        verbose_name='कुल खर्च मध्ये उपभोक्ता समिति मार्फत भएको रकम')
    construction_business_expense = models.FloatField(
        verbose_name='निर्माण व्यवसायीबाट भएको रकम')

    def __str__(self):
        return str(self.program)
