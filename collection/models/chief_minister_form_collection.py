from django.db import models
from django.db.models.enums import Choices

from forms.models.risk_allowance import RiskAllowance
from forms.models.fund_receipt_expense import FundReceiptExpense
from forms.models.epidemic_outbreak_preparatory_work import EpidemicOutbreakPreparatoryWork
# from forms.models.action_plan_implementation import ActionPlanImplementation

from users.models.user import User
from collection.utils import INTERNAL_AFFAIRS_STATE, STATUS

class InternalAffairFormCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(choices=INTERNAL_AFFAIRS_STATE, default=0, blank=True)
    status = models.CharField(choices=STATUS, default='started', max_length=20)
    
    risk_allowance = models.OneToOneField(
        RiskAllowance, on_delete=models.CASCADE, null=True)
    fund_receipt_expense = models.OneToOneField(
        FundReceiptExpense, on_delete=models.CASCADE, null=True)
    epidemic_outbreak_prep = models.OneToOneField(
        EpidemicOutbreakPreparatoryWork, on_delete=models.CASCADE, null=True)
    # action_plan_implementation = models.OneToOneField(
    #     ActionPlanImplementation, on_delete=models.CASCADE, null=True)
    


    def __str__(self):
        display_name = f"{self.user.body} ({self.get_state_display()})"
        return display_name
