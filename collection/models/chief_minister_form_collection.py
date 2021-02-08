from django.db import models
from django.db.models.enums import Choices

from forms.models.risk_allowance import RiskAllowance
from forms.models.fund_receipt_expense import FundReceiptExpense
from forms.models.epidemic_outbreak_preparatory_work import EpidemicOutbreakPreparatoryWork
from forms.models.province_institution_management import ProvinceInstitutionManagement
from forms.models.action_plan_implementation import ActionPlanImplementation

from master_data.models import FiscalYear, Province, GovernmentBody

from users.models.user import User
from collection.utils import CHIEF_MINISTER_STATE, STATUS

class ChiefMinisterOfficeFormCollection(models.Model):
    province = models.ForeignKey(Province, on_delete=models.PROTECT, null=True, blank=False)
    body = models.ForeignKey(GovernmentBody, on_delete=models.PROTECT, blank=True, null=True)
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.PROTECT, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(choices=CHIEF_MINISTER_STATE, default=0, blank=True)
    status = models.CharField(choices=STATUS, default='started', max_length=20)
    approver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='chief_minister_approver')
    reject_msg = models.CharField(null=True, blank=True, max_length=250)
    
    risk_allowance = models.OneToOneField(
        RiskAllowance, on_delete=models.CASCADE, null=True)
    fund_receipt_expense = models.OneToOneField(
        FundReceiptExpense, on_delete=models.CASCADE, null=True)
    epidemic_outbreak_prep = models.OneToOneField(
        EpidemicOutbreakPreparatoryWork, on_delete=models.CASCADE, null=True)
    province_institute_management = models.OneToOneField(
        ProvinceInstitutionManagement, on_delete=models.CASCADE, null=True)
    action_plan_implementation = models.OneToOneField(
        ActionPlanImplementation, on_delete=models.CASCADE, null=True)


    def __str__(self):
        display_name = f"{self.user.body} ({self.get_state_display()})"
        return display_name
