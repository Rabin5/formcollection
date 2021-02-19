from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES
from master_data.models import FiscalYear, GovernmentBody, ExpenseHeader


class FundOperation(FormBaseModel):

    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT,
                                    related_name='fund_operation', null=True, verbose_name='आर्थिक बर्ष: ')
    body = models.ForeignKey(GovernmentBody, on_delete=models.PROTECT,
                             related_name="fund_operation", null=True, verbose_name='निकायको नामः: ')
    state = models.CharField(
        max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return self.body.name


class FundOperationLine(FormLineBaseModel):
    fund_operation = models.ForeignKey(
        FundOperation, on_delete=models.CASCADE, related_name='lines')
    body = models.CharField(
        max_length=300,
        blank=False,
        null=True,
        verbose_name="उपलब्ध गराउने निकाय"
    )
    amt_received = models.FloatField(verbose_name="प्राप्त रकम")
    expense_header = models.ForeignKey(
        ExpenseHeader, on_delete=models.CASCADE, related_name='fund_operation_line', verbose_name="खर्चको शीर्षक")
    amt_expensed = models.FloatField(verbose_name="खर्च रकम")

    def __str__(self):
        return self.expense_header.title
