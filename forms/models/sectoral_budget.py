from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS


class SectoralBudget(FormBaseModel):
    pass


class SectoralBudgetLine(FormLineBaseModel):
    main_area =models.CharField(max_length=300,verbose_name='मुख्य क्षेत्र')
    yearly_budget = models.FloatField(verbose_name='वार्षिक वजेट')
    expensed_amount = models.FloatField(verbose_name='खर्च रकम')
    percentage_of_total_expenditure = models.FloatField(verbose_name='कुल खर्च मध्ये प्रतिशत')
    sectoral_budget = models.ForeignKey(
        SectoralBudget, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')