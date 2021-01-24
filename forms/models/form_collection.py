from django.db import models
from django.db.models.enums import Choices

from .risk_allowance import RiskAllowance
from .epidemic_outbreak_preparatory_work import EpidemicOutbreakPreparatoryWork
from .action_plan_implementation import ActionPlanImplementation
from .medical_expense import MedicalExpense
from .medical_receipt import MedicalReceipt
from .medical_use import MedicalUse
from .pcr_test_compliance_detail import PcrTestComplianceDetail
from .rdttestdetail import RdtTestDetail
from .fund_receipt_expense import FundReceiptExpense
from .med_purchase_desc import MedicalPurchaseDescription
from .pcr_lab_detail import PcrLaboratoryDetail
from .pcr_kit_usage import PcrKitUsage
from .covid_hos_equip import CovidHospitalEquipment

from users.models.user import User
from forms.utils import CH_STATE, STATUS


class FormCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(choices=CH_STATE, default=1, blank=True)
    status = models.CharField(choices=STATUS, default='started', max_length=20)
    medical_expense = models.OneToOneField(
        MedicalExpense, on_delete=models.CASCADE, null=True)
    risk_allowance = models.OneToOneField(
        RiskAllowance, on_delete=models.CASCADE, null=True)
    medical_receipt = models.OneToOneField(
        MedicalReceipt, on_delete=models.CASCADE, null=True)
    medical_use = models.OneToOneField(
        MedicalUse, on_delete=models.CASCADE, null=True)
    pcr_test_compliance_detail = models.OneToOneField(
        PcrTestComplianceDetail, on_delete=models.CASCADE, null=True)
    rdt_test_detail = models.OneToOneField(
        RdtTestDetail, on_delete=models.CASCADE, null=True)
    fund_receipt_expense = models.OneToOneField(
        FundReceiptExpense, on_delete=models.CASCADE, null=True)
    med_purchase_desc = models.OneToOneField(
        MedicalPurchaseDescription, on_delete=models.CASCADE, null=True)
    pcr_lab_detail = models.OneToOneField(
        PcrLaboratoryDetail, on_delete=models.CASCADE, null=True)
    pcr_kit_usage = models.OneToOneField(
        PcrKitUsage, on_delete=models.CASCADE, null=True)
    epidemic_outbreak_preparatory_work = models.OneToOneField(
        EpidemicOutbreakPreparatoryWork, on_delete=models.CASCADE, null=True)
    action_plan_implementation=models.OneToOneField(ActionPlanImplementation,on_delete=models.CASCADE,null=True)
    # cov_hos_equipment = models.OneToOneField(CovidHospitalEquipment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        display_name = f"{self.user.body} ({self.get_state_display()})"
        return display_name
