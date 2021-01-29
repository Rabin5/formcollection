from django.db import models
from django.db.models.enums import Choices

from forms.models.epidemic_outbreak_preparatory_work import EpidemicOutbreakPreparatoryWork
from forms.models.medical_expense import MedicalExpense
from forms.models.medical_receipt import MedicalReceipt
from forms.models.medical_use import MedicalUse
from forms.models.fund_receipt_expense import FundReceiptExpense
from forms.models.med_purchase_desc import MedicalPurchaseDescription
from forms.models.case_investigation_tracing import CaseInvestigationTracing
from forms.models.covid_hospital_manpower import CovidHospitalManpower
from forms.models.covid_hos_equip import CovidHospitalEquipment
from forms.models.quarantine_management_detail import QuarantineManagementDetail
from forms.models.isolationmanagementdetail import IsolationManagementDetail
from forms.models.quarantine_construct_expenditure import QuarantineConstructionExpenditure
from forms.models.isolationconstructionexpenditure import IsolationConstructionExependiture
from forms.models.received_relief_detail import ReceivedReliefDetail
from forms.models.ward_relief_procure_distribution import WardReliefProcureDistribution
from forms.models.relief_distribution_expense import ReliefDistributionExpense
from forms.models.action_plan_implementation import ActionPlanImplementation

from users.models.user import User
from collection.utils import PROVINCE_STATE, STATUS

class ProvinceFormCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(choices=PROVINCE_STATE, default=0, blank=True)
    status = models.CharField(choices=STATUS, default='started', max_length=20)
    
    epidemic_outbreak_prep = models.OneToOneField(
        EpidemicOutbreakPreparatoryWork, on_delete=models.CASCADE, null=True)
    fund_receipt_expense = models.OneToOneField(
        FundReceiptExpense, on_delete=models.CASCADE, null=True)
    medical_expense = models.OneToOneField(
        MedicalExpense, on_delete=models.CASCADE, null=True)
    risk_allowance = models.OneToOneField(
        RiskAllowance, on_delete=models.CASCADE, null=True)
    medical_receipt = models.OneToOneField(
        MedicalReceipt, on_delete=models.CASCADE, null=True)
    medical_use = models.OneToOneField(
        MedicalUse, on_delete=models.CASCADE, null=True)
    med_purchase_desc = models.OneToOneField(
        MedicalPurchaseDescription, on_delete=models.CASCADE, null=True)



    pcr_test_compliance_detail = models.OneToOneField(
        PcrTestComplianceDetail, on_delete=models.CASCADE, null=True)
    rdt_test_detail = models.OneToOneField(
        RdtTestDetail, on_delete=models.CASCADE, null=True)
    
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
    isolation_construction_expenditure = models.OneToOneField(
        IsolationConstructionExependiture, on_delete=models.CASCADE, null=True)
    district_covid_management = models.OneToOneField(
        DistrictCovidManagement, on_delete=models.CASCADE, null=True)
    fund_operation = models.OneToOneField(
        FundOperation, on_delete=models.CASCADE, null=True)


    def __str__(self):
        display_name = f"{self.user.body} ({self.get_state_display()})"
        return display_name
