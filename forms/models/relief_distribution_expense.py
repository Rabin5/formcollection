from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES
from master_data.models import FiscalYear, GovernmentBody, ReliefType


class ReliefDistributionExpense(FormBaseModel):

    fiscal_year = models.ForeignKey(
        FiscalYear,
        on_delete=models.PROTECT,
        related_name='reliefdistribution',
        null=True,
        verbose_name='आर्थिक बर्ष'
    )
    body = models.ForeignKey(
        GovernmentBody,
        on_delete=models.PROTECT,
        related_name="reliefdistribution",
        null=True,
        verbose_name='निकायको नाम'
    )
    state = models.CharField(
        max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return self.body.name


class ReliefDistributionExpenseLine(FormLineBaseModel):
    relief_distribution = models.ForeignKey(
        ReliefDistributionExpense,
        on_delete=models.CASCADE,
        related_name='lines'
    )
    amt_expense = models.FloatField(
        verbose_name="खर्च रकम"
    )
    relief_type = models.ForeignKey(
        ReliefType,
        on_delete=models.CASCADE,
        related_name='reliefdistributionline',
        verbose_name="राहातको प्रकार"
    )
    num_relif_beneficiary = models.IntegerField(
        verbose_name='राहात पाउनेको संख्या')
    remarks = models.CharField(
        max_length=100, verbose_name='कैफियत')

    def __str__(self):
        return self.relief_type.title
