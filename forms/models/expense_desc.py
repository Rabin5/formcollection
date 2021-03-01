from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS


class ExpenseDesc(FormBaseModel):
    pass


class ExpenseDescLine(FormLineBaseModel):
    gross_internal_income = models.FloatField(verbose_name='कूल आन्तरिक आय')
    official_expense = models.FloatField(verbose_name='प्रशासनिक खर्च')
    financial_support_expense = models.FloatField(
        verbose_name='आथिंक सहायता खर्च')
    future_expense = models.FloatField(verbose_name='भैपरी आउने खर्च')
    capital_expenditure = models.FloatField(verbose_name='पूजीगत खर्च')
    expense_desc = models.ForeignKey(
        ExpenseDesc, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
