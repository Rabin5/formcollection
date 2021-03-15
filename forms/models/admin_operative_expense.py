from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS



class AdminOperativeExpense(FormBaseModel):
    amt_operational_expenses = models.FloatField(verbose_name='संचालन खर्च रु. ')


class AdminOperativeExpenseLine(FormLineBaseModel):
    designation=models.CharField(max_length=255, verbose_name='पद')
    monthly_salary_expense = models.FloatField(verbose_name='मासिक तलब खर्च रु. ')
    total_expense_pre_previous_fy = models.FloatField(verbose_name='जम्मा खर्च रु. २०७५ /७६ ')
    total_expense_previous_fy = models.FloatField(verbose_name='जम्मा खर्च रु. २०७६ /७७ ')
    total_expense_current_fy = models.FloatField(verbose_name='जम्मा खर्च रु. २०७७ /७८ ')
    
    admin_op_expense_line = models.ForeignKey(
        AdminOperativeExpense, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')
