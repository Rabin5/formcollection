from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
import nepali_datetime
import datetime


class BudgetSubmitApproval(FormBaseModel):
    pass


class BudgetSubmitApprovalLine(FormLineBaseModel):
    budgetsubmitapproval_line = models.ForeignKey(
        BudgetSubmitApproval, on_delete=models.CASCADE, related_name='lines')
    desc = models.CharField(max_length=300, verbose_name='विवरण')
    date = models.CharField(max_length=300, verbose_name='मिति र रकम')
    # amount = models.DecimalField(
    #     verbose_name='रकम')
    total_budget = models.CharField(
        max_length=300, verbose_name='कुल बजेट')
    amount = models.FloatField(verbose_name='रकम')

    def __str__(self):
        return self.desc
