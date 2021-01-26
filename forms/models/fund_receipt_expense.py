from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, GovernmentBody, SourceBudget, ExpenseHeader, get_current_fy


class FundReceiptExpense(FormBaseModel):
    """
    Model for form class: 1_covid_hospital/1.puml
    Code: fre
    """

    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नाम')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='fund_receipt_expenses', verbose_name='आर्थिक बर्ष')
    fiscal_year_from = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, related_name='fre_fy_from', null=True, verbose_name='सुरु आर्थिक वर्ष', default=get_current_fy)
    fy_month_from = models.IntegerField(choices=BS_MONTHS, default=4, verbose_name='सुरु महिना')
    fiscal_year_to = models.ForeignKey(FiscalYear, on_delete=models.RESTRICT, related_name='fre_fy_to', null=True, verbose_name='अन्त्य आर्थिक वर्ष', default=get_current_fy)
    fy_month_to = models.IntegerField(choices=BS_MONTHS, default=3, verbose_name='अन्त्य महिना')
    state = models.CharField(max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return f'{self.fiscal_year_from} '
        # return f'{self.fiscal_year_from} {self.get_fy_month_from_display()} to {self.fiscal_year_to} {self.get_fy_month_to_display}'


class FundReceiptExpenseLine(FormLineBaseModel):
    receipt_expense = models.ForeignKey(FundReceiptExpense, on_delete=models.CASCADE, related_name='lines', verbose_name='')
    budget_source = models.ForeignKey(SourceBudget, on_delete=models.PROTECT, verbose_name='बजेट/आम्दानीको स्रोत')
    expense_header = models.ForeignKey(ExpenseHeader, on_delete=models.PROTECT, verbose_name='खर्च शीर्षक')
    fy_start_received_amt = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='सुरुवात महिनासम्म प्राप्त रकम')
    fy_end_received_amt = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='अन्त्य महिनासम्म प्राप्त रकम')
    fy_start_expense_amt = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='सुरुवात महिनासम्म खर्च रकम')
    fy_end_expense_amt = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='अन्त्य महिनासम्म खर्च रकम')
