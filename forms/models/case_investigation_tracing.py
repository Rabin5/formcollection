from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models import GovernmentBody, FiscalYear
from collection.utils import STATES


class CaseInvestigationTracing(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नामः')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='case_investigation', verbose_name='आर्थिक बर्ष: ')

    state = models.CharField(
        max_length=25, choices=STATES, default='draft', blank=True)

    def __str__(self):
        return self.body.name


class CaseInvestigationTracingLine(FormLineBaseModel):
    case_investigation_tracing = models.ForeignKey(
        CaseInvestigationTracing, on_delete=models.PROTECT, verbose_name='केस अनुसन्धान ट्रेसिंग')
    description = models.TextField(verbose_name='बिबरण')
    num_team_members = models.PositiveIntegerField(
        verbose_name='टिम गठन संख्या ')
    amount_expense = models.FloatField(verbose_name='खर्च रकम')
    num_searched_cases = models.IntegerField(
        verbose_name='खोज पडताल गरिएका केश संख्या')
    num_identified_infection = models.IntegerField(
        verbose_name='खोज पडतालबाट पहिचान भएका संक्रमित')
    remarks = models.CharField(max_length=200, verbose_name='कैफियत')

    def __str__(self):
        return self.case_investigation_tracing.body.name
