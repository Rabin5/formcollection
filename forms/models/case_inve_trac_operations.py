from django.db import models

from forms.abstract import FormBaseModel, FormLineBaseModel
from master_data.models import FiscalYear
from master_data.models.government import GovernmentBody


class CaseInvestigationTracingOperations(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, related_name='case_inves_tracing_operation_body', verbose_name='निकायको नामः: ')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='_tracing_operation_fiscal_year', verbose_name='आर्थिक बर्ष: ')

    def __str__(self):
        return self.body.name


class CaseInvestigationTracingOperationsLine(FormLineBaseModel):
    case_invs_body = models.ForeignKey(
        GovernmentBody, on_delete=models.CASCADE, related_name='case_investigation_body', verbose_name='निकायको नामः: ')
    num_team_members = models.IntegerField(
        blank=True, null=True, verbose_name='टीमको सदस्य संख्या')
    amt_expense = models.FloatField(
        blank=True, null=True, verbose_name='खर्च रकम')
    num_case = models.IntegerField(
        blank=True, null=True, verbose_name='केश अनुसन्धान संख्या')
    num_contact_identified = models.IntegerField(
        blank=True, null=True, verbose_name='कन्टयाक्टमाआएकाव्यक्तिहरूकोपहीचान संख्या')
    num_consult_refer = models.IntegerField(
        blank=True, null=True, verbose_name='सामान्य परामर्श, फलोअप तथा रेफर संख्या')
    num_sample_collect_test = models.IntegerField(
        blank=True, null=True, verbose_name='नमूना संकलन वा द्रुत परिक्षण संख्या')
    caseinvestigationtracingoperations_line = models.ForeignKey(
        CaseInvestigationTracingOperations, on_delete=models.CASCADE)
