from django.db import models
from django.db.models.enums import Choices
from forms.utils import CH_STATE, STATUS
from users.models.user import User

from .covid_hos_equip import CovidHospitalEquipment
from .covid_hospital_manpower import CovidHospitalManpower
from .covidhospitaldetail import CovidHospitalDetail
from .fund_receipt_expense import FundReceiptExpense
from .isolationmanagementdetail import IsolationManagementDetail
from .med_purchase_desc import MedicalPurchaseDescription
from .medical_expense import MedicalExpense
from .medical_receipt import MedicalReceipt
from .medical_use import MedicalUse
from .pcr_kit_usage import PcrKitUsage
from .pcr_lab_detail import PcrLaboratoryDetail
from .pcr_test_compliance_detail import PcrTestComplianceDetail
from .rdttestdetail import RdtTestDetail
from .risk_allowance import RiskAllowance


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
    covid_hos_mainpower = models.OneToOneField(
        CovidHospitalManpower, on_delete=models.CASCADE, null=True)
    covid_hospital_detail = models.OneToOneField(
        CovidHospitalDetail, on_delete=models.CASCADE, null=True)
    IsolationManagementDetail = models.OneToOneField(
        IsolationManagementDetail, on_delete=models.CASCADE, null=True)
    cov_hos_equipment = models.OneToOneField(
        CovidHospitalEquipment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        display_name = f"{self.user.body} ({self.get_state_display()})"
        return display_name
