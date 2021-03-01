from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import Consultant


class DPRExpense(FormBaseModel):
    pass


class DPRExpenseLine(FormLineBaseModel):
    program_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='कार्यक्रमको नाम')
    consultant = models.ForeignKey(Consultant, verbose_name="परामर्शदाता", on_delete=models.CASCADE)
    approved_budget = models.FloatField(verbose_name='स्वीकृत बजेट')
    amt_expense = models.FloatField(verbose_name='खर्च रकम')
    determined_budget = models.FloatField(verbose_name='अध्ययनबाट निर्धारण भएका आयोजनाको लागत')    
    drp_expense_line = models.ForeignKey(
        DPRExpense, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
