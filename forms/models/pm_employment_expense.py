from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models.fiscal_year import FiscalYear

class PMEmploymentExpense(FormBaseModel):
    pass


class PMEmploymentExpenseLine(FormLineBaseModel):
    pm_employment_line = models.ForeignKey(
        PMEmploymentExpense, on_delete=models.CASCADE, related_name='lines')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.CASCADE, verbose_name='आर्थिक बर्ष')
    budget = models.FloatField(verbose_name='बजेट रु.')
    expense = models.FloatField(verbose_name='खर्च रु.')
    worker_wage = models.FloatField(verbose_name='श्रमिक ज्याला खर्च रु.')
    

    def __str__(self):
        return str(self.fiscal_year.name)
