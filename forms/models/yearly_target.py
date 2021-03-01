from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS


class YearlyTarget(FormBaseModel):
    pass


class YearlyTargetLine(FormLineBaseModel):
    plan = models.CharField(max_length=255, blank=True, null=True, verbose_name='कार्यक्रम / योजना')
    amt_expense = models.FloatField(verbose_name='यो वर्ष खर्च')
    financial_progress = models.FloatField(verbose_name='वित्तिय प्रगति')
    physical_progress = models.FloatField(verbose_name='भौतिक प्रगति')
    description = models.TextField(blank=True, null=True, verbose_name='७५% भन्दा न्युन प्रगति भएकोमा सो को कारण')
    yearly_target_line = models.ForeignKey(
        YearlyTarget, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
