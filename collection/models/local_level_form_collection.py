from django.db import models
from django.db.models.enums import Choices

from forms.models.epidemic_outbreak_preparatory_work import EpidemicOutbreakPreparatoryWork
from forms.models.medical_expense import MedicalExpense
from forms.models.medical_receipt import MedicalReceipt
from forms.models.medical_use import MedicalUse
from forms.models.risk_allowance import RiskAllowance
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
from forms.models.case_inve_trac_operations import CaseInvestigationTracingOperations
from forms.models.reliefprocuredistribution import ReliefProcureDistribution
from forms.models.reliefprocurementdetail import ReliefProcurementDetail


from users.models.user import User
from collection.utils import LOCAL_LEVEL_STATE, STATUS

class LocalLevelFormCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(choices=LOCAL_LEVEL_STATE, default=0, blank=True)
    status = models.CharField(choices=STATUS, default='started', max_length=20)
    approver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='local_level_approver')
    reject_msg = models.CharField(null=True, blank=True, max_length=250)
    
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
    isolation_management_detail = models.OneToOneField(
        IsolationManagementDetail, on_delete=models.CASCADE, null=True)
    cov_hos_equipment = models.OneToOneField(
        CovidHospitalEquipment, on_delete=models.CASCADE, null=True)
    covid_hos_mainpower = models.OneToOneField(
        CovidHospitalManpower, on_delete=models.CASCADE, null=True)
    quarantine_management_detail = models.OneToOneField(
        QuarantineManagementDetail, on_delete=models.CASCADE, null=True)
    quarantine_contruction_expenditure = models.OneToOneField(
        QuarantineConstructionExpenditure, on_delete=models.CASCADE, null=True)
    isolation_construction_expenditure = models.OneToOneField(
        IsolationConstructionExependiture, on_delete=models.CASCADE, null=True)
    case_investigation_tracing = models.OneToOneField(
        CaseInvestigationTracing, on_delete=models.CASCADE, null=True)
    case_investigation_tracing_operation = models.OneToOneField(
        CaseInvestigationTracingOperations, on_delete=models.CASCADE, null=True)
    relief_procurement_detail = models.OneToOneField(
        ReliefProcurementDetail, on_delete=models.CASCADE, null=True)
    relief_procurement_distribution = models.OneToOneField(
        ReliefProcureDistribution, on_delete=models.CASCADE, null=True)
    ward_relief_procurement_dist = models.OneToOneField(
        WardReliefProcureDistribution, on_delete=models.CASCADE, null=True)
    received_relief_detail = models.OneToOneField(
        ReceivedReliefDetail, on_delete=models.CASCADE, null=True)
    relief_distribution_expense = models.OneToOneField(
        ReliefDistributionExpense, on_delete=models.CASCADE, null=True)
    action_plan_implementation = models.OneToOneField(
        ActionPlanImplementation, on_delete=models.CASCADE, null=True)


    def __str__(self):
        display_name = f"{self.user.body} ({self.get_state_display()})"
        return display_name
