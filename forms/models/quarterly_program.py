from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS



class QuarterlyProgram(FormBaseModel):
    pass


class QuarterlyProgramLine(FormLineBaseModel):
    budget_subtiles = models.FloatField(verbose_name='बजेट उपशीर्षक')
    total_expense = models.FloatField(verbose_name='कुल खर्च')
    first_quarter_expense = models.FloatField(verbose_name='प्रथम चौमासिक खर्च')
    second_quarter_expense = models.FloatField(verbose_name='दोस्रो चौमासिक खर्च')
    third_quarter_expense = models.FloatField(verbose_name='तेस्रो चौमासिक खर्च')
    fiscal_month_expense = models.FloatField(verbose_name='आषाढ महिना चौमासिक खर्च')    
    quarterly_program_line = models.ForeignKey(
        QuarterlyProgram, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
