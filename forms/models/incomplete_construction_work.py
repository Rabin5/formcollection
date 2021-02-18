from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import ConstructionCompany
from master_data.models.government import GovernmentBody


class IncompleteConstructionWork(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नाम')

    def __str__(self):
        return self.body.name


class IncompleteConstructionWorkLine(FormLineBaseModel):
    construction_work = models.CharField(max_length=255, blank=True, null=True, verbose_name='निर्माण कार्य')
    construction_company = models.ForeignKey(
        ConstructionCompany, on_delete=models.PROTECT, verbose_name='निर्माण व्यवसायी')
    agreement_date = models.DateField(null=True, blank=False)
    estimated_completion_date = models.DateField(null=True, blank=False)
    expense = models.FloatField(verbose_name='यो वर्ष सम्मको खर्च')
    progress = models.CharField(max_length=255, blank=True, null=True, verbose_name='भौतिक प्रगति')
    incomplete_construction_work_line = models.ForeignKey(
        IncompleteConstructionWork, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
