from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS


class ExpenditureExceedingAllocation(FormBaseModel):
    pass


class ExpenditureExceedingAllocationLine(FormLineBaseModel):
    title =models.CharField(max_length=300,verbose_name='शीर्षक')
    appropriated_amt= models.FloatField(verbose_name='विनियोजित रकम')
    expense_amt= models.FloatField(verbose_name='खर्च भएको रकम')
    expense_exceeded_amt = models.FloatField(verbose_name='बढी खर्च भएको रकम')
    expenditure_exceeding_allocation = models.ForeignKey(
        ExpenditureExceedingAllocation, null=True, blank=True, on_delete=models.PROTECT, related_name='lines')