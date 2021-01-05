from django.db import models
from .medical_expense import MedicalExpense
from .risk_allowance import RiskAllowance


class FormCollection(models.Model):
    med_exp = models.OneToOneField(MedicalExpense, on_delete=models.CASCADE, null=True)
    risk_allowance = models.OneToOneField(RiskAllowance, on_delete=models.CASCADE, null=True)