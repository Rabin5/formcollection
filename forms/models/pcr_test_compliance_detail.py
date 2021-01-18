from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, Product
from master_data.models.government import GovernmentBody
from forms.utils import BS_MONTHS


class PcrTestComplianceDetail(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नामः: ')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='pctr_test_fiscal_year', verbose_name='आर्थिक बर्ष: ')

    def __str__(self):
        return self.body.name


choices = BS_MONTHS


class PcrTestComplianceDetailLine(FormLineBaseModel):
    month = models.IntegerField(
        choices=choices, blank=True, null=True, verbose_name='महिना')
    year = models.IntegerField(verbose_name='बर्ष:')
    all_area_test_num = models.IntegerField(
        verbose_name='सबै क्षेत्रमा गरेको कुल परीक्षण संख्या')
    all_area_infected_num = models.IntegerField(
        verbose_name='सबै क्षेत्रमा गरेको कुल  संक्रमित संख्या')
    priority_1_test_num = models.IntegerField(
        verbose_name='Priority-1क्षेत्रमा गरेको परीक्षण संख्या')
    priority_1_infected_num = models.IntegerField(
        verbose_name='Priority-1 क्षेत्रमा गरेको संक्रमित संख्या')
    priority_2_test_num = models.IntegerField(
        verbose_name='Priority-2 क्षेत्रमा गरेको परीक्षण संख्या')
    priority_2_infected_num = models.IntegerField(
        verbose_name='Priority-2 क्षेत्रमा गरेको संक्रमित संख्या')
    priority_3_test_num = models.IntegerField(
        verbose_name='Priority-3 क्षेत्रमा गरेको परीक्षण संख्या')
    priority_3_infected_num = models.IntegerField(
        verbose_name='Priority-3 क्षेत्रमा गरेको संक्रमित संख्या')
    non_priority_test_num = models.IntegerField(
        verbose_name='Non-priority  क्षेत्रमा गरेको परीक्षण संख्या')
    non_priority_infected_num = models.IntegerField(
        verbose_name='Non-priority  क्षेत्रमा गरेको संक्रमित संख्या')
    pcrtest_compliance_detail = models.ForeignKey(
        PcrTestComplianceDetail, on_delete=models.PROTECT)
