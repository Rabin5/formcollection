from django.db import models
from forms.abstract import FormBaseModel, FormLineBaseModel
from collection.utils import STATES, BS_MONTHS
from master_data.models import ConstructionCompany
from master_data.models.government import GovernmentBody
from master_data.models.fiscal_year import FiscalYear


class CashForWork(FormBaseModel):
    pass


class CashForWorkLine(FormLineBaseModel):
    cashforwork_line = models.ForeignKey(
        CashForWork, on_delete=models.CASCADE, null=True, blank=True, related_name='lines')
    formulated_plans = models.TextField(verbose_name='तर्जुमा गरेको योजनाहरु')
    estimated_cost = models.FloatField(verbose_name='लागत अनुमान रु.')
    is_included = models.BooleanField(
        verbose_name='वार्षिक नीति तथा कार्यक्रममा समावेश भएको छ / छैन')
    estimated_num_jobs = models.IntegerField(
        verbose_name='उपलव्ध हुने अनुमानीत रोजगारी संख्या')
    jobs_pre_previous_fy = models.IntegerField(
        verbose_name='हालसम्म उपलव्ध भएको रोजगारी संख्या २०७५ /७६')
    jobs_previous_fy = models.IntegerField(
        verbose_name='हालसम्म उपलव्ध भएको रोजगारी संख्या २०७६ /७७')
    jobs_current_fy = models.IntegerField(
        verbose_name='हालसम्म उपलव्ध भएको रोजगारी संख्या २०७७ /७८')
    expense_jobs_pre_previous_fy = models.FloatField(
        verbose_name='रोजगारी प्रधान गरीएको खर्च रु २०७५ /७६')
    expense_jobs_previous_fy = models.FloatField(
        verbose_name='रोजगारी प्रधान गरीएको खर्च रु २०७६ /७७')
    expense_jobs_current_fy = models.FloatField(
        verbose_name='रोजगारी प्रधान गरीएको खर्च रु २०७७ /७८')

    def __str__(self):
        return self.formulated_plans
