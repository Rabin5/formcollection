from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from forms.utils import STATES, BS_MONTHS
from master_data.models import FiscalYear, Product
from master_data.models.company import Laboratory
from master_data.models.government import GovernmentBody
from forms.utils import BS_MONTHS


class RdtTestDetail(FormBaseModel):
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, verbose_name='निकायको नामः: ')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, related_name='rdt_test_fiscal_year', verbose_name='आर्थिक बर्ष: ')

    def __str__(self):
        return self.fiscal_year


class RdtTestDetailLine(FormBaseModel):
    laboratory = models.ForeignKey(
        Laboratory, on_delete=models.PROTECT, verbose_name='ल्यावको नाम र स्थान')
    num_tested_fy_end = models.IntegerField(
        verbose_name='आषाढ मसान्तसम्म आरडीटी परीक्षण गरेको संख्या')
    num_tested_pcr = models.IntegerField(
        verbose_name='परीक्षण मध्ये पिसीआर गरिएको संख्या')
    expense_rdt_test = models.IntegerField(
        verbose_name='आरडीटी परीक्षणमा आषाढ समान्त सम्म भएको खर्च')

    rdt_test_detail = models.ForeignKey(
        RdtTestDetail, on_delete=models.PROTECT)

    def __str__(self):
        return self.laboratory
