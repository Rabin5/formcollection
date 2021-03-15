from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear


class MeetingDetail(FormBaseModel):
    pass


class MeetingDetailLine(FormLineBaseModel):
    fiscal_year=models.ForeignKey(FiscalYear, verbose_name='आर्थिक बर्ष', on_delete=models.PROTECT)
    meeting_date = models.DateField(verbose_name='बैठक बसेको मितिहरू')
    meeting_conclusion = models.TextField(verbose_name='बैठकको निर्णयहरु')
    
    meeting_detail_line = models.ForeignKey(
        MeetingDetail, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
