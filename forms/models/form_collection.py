from django.db import models
from .medical_expense import MedicalExpense
from .risk_allowance import RiskAllowance
from users.models.user import User
from forms.utils import CH_STATE

class FormCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(max_length=25, choices=CH_STATE, default=1, blank=True)
    med_exp = models.OneToOneField(MedicalExpense, on_delete=models.CASCADE, null=True)
    risk_allowance = models.OneToOneField(RiskAllowance, on_delete=models.CASCADE, null=True)
    
