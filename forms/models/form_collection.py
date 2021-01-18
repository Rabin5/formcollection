from django.db import models
from django.db.models.enums import Choices

from .risk_allowance import RiskAllowance
from .medical_expense import MedicalExpense
from .medical_receipt import MedicalReceipt
from .medical_use import MedicalUse
from .pcr_test_compliance_detail import PcrTestComplianceDetail
from .rdttestdetail import RdtTestDetail
from .fund_receipt_expense import FundReceiptExpense
    
from users.models.user import User
from forms.utils import CH_STATE, STATUS

class FormCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(choices=CH_STATE, default=1, blank=True)
    status = models.CharField(choices=STATUS, default='started', max_length=20)
    medical_expense = models.OneToOneField(MedicalExpense, on_delete=models.CASCADE, null=True)
    risk_allowance = models.OneToOneField(RiskAllowance, on_delete=models.CASCADE, null=True)
    medical_receipt = models.OneToOneField(MedicalReceipt, on_delete=models.CASCADE, null=True)
    medical_use = models.OneToOneField(MedicalUse, on_delete=models.CASCADE, null=True)
    pcr_test_compliance_detail = models.OneToOneField(PcrTestComplianceDetail, on_delete=models.CASCADE, null=True)
    rdt_test_detail = models.OneToOneField(RdtTestDetail, on_delete=models.CASCADE, null=True)
    fund_receipt_expense = models.OneToOneField(FundReceiptExpense, on_delete=models.CASCADE, null=True)

    def __str__(self):
        display_name = f"{self.user.body} ({self.get_state_display()})"
        return display_name
    