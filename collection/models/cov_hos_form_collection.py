from django.db import models
from django.db.models.enums import Choices

from forms.models.covid_hospital_manpower import CovidHospitalManpower
from forms.models.covidhospitaldetail import CovidHospitalDetail
from forms.models.isolationmanagementdetail import IsolationManagementDetail
from forms.models.medical_expense import MedicalExpense
from forms.models.medical_receipt import MedicalReceipt
from forms.models.medical_use import MedicalUse
from forms.models.pcr_test_compliance_detail import PcrTestComplianceDetail
from forms.models.rdttestdetail import RdtTestDetail
from forms.models.risk_allowance import RiskAllowance
from forms.models.fund_receipt_expense import FundReceiptExpense
from forms.models.med_purchase_desc import MedicalPurchaseDescription
from forms.models.pcr_lab_detail import PcrLaboratoryDetail
from forms.models.pcr_kit_usage import PcrKitUsage
from forms.models.covid_hos_equip import CovidHospitalEquipment
from forms.models.quarantine_management_detail import QuarantineManagementDetail
from forms.models.quarantine_construct_expenditure import QuarantineConstructionExpenditure
from forms.models.cov_hos_management_checklist import CovidHospitalManagementChecklist
from forms.models.isolationconstructionexpenditure import IsolationConstructionExependiture

from users.models.user import User
from collection.utils import CH_STATE, STATUS

class CovHosFormCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(choices=CH_STATE, default=0, blank=True)
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
    isolation_management_detail = models.OneToOneField(
        IsolationManagementDetail, on_delete=models.CASCADE, null=True)
    cov_hos_equipment = models.OneToOneField(
        CovidHospitalEquipment, on_delete=models.CASCADE, null=True)
    quarantine_management_detail = models.OneToOneField(
        QuarantineManagementDetail, on_delete=models.CASCADE, null=True)
    quarantine_contruction_expenditure = models.OneToOneField(
        QuarantineConstructionExpenditure, on_delete=models.CASCADE, null=True)
    cov_hos_management_checklist = models.OneToOneField(
        CovidHospitalManagementChecklist, on_delete=models.CASCADE, null=True)
    isolation_construction_expenditure = models.OneToOneField(
        IsolationConstructionExependiture, on_delete=models.CASCADE, null=True)

    def __str__(self):
        display_name = f"{self.user.body} ({self.get_state_display()})"
        return display_name
