from django.db import models
from django.db.models.enums import Choices
from .medical_expense import MedicalExpense
from .risk_allowance import RiskAllowance
from users.models.user import User
from forms.utils import CH_STATE, STATUS

class FormCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(choices=CH_STATE, default=1, blank=True)
    med_exp = models.OneToOneField(MedicalExpense, on_delete=models.CASCADE, null=True)
    risk_allowance = models.OneToOneField(RiskAllowance, on_delete=models.CASCADE, null=True)
    status = models.CharField(choices=STATUS, default='started', max_length=20)

    def __str__(self):
        display_name = f"{self.user.body} ({self.get_state_display()})"
        return display_name
    
