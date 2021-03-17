from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import ConstructionCompany
from master_data.models.government import GovernmentBody
from master_data.models.fiscal_year import FiscalYear
from master_data.models.industry import Industry


class IndustryFinancialIncentive(FormBaseModel):
    pass


class IndustryFinancialIncentiveLine(FormLineBaseModel):
    industryfinancialincentive_line = models.ForeignKey(
        IndustryFinancialIncentive, on_delete=models.CASCADE, null=True, blank=True, related_name='lines')
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.CASCADE, verbose_name='आर्थिक वर्ष')

    industry_name = models.ForeignKey(
        Industry, on_delete=models.PROTECT, verbose_name='उधोग प्रतिष्ठानको नाम')
    total_job_opening = models.IntegerField(
        verbose_name='माग भएको प्रशिक्षार्थी श्रमिक संख्या')
    financial_incentive_amount = models.FloatField(
        verbose_name='यो वर्ष सम्मको खर्च')

    def __str__(self):
        return self.industry_name.name
