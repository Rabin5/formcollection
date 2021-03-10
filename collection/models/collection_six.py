from django.db import models
from django.db.models.enums import Choices

from forms.models.procurement_auditor import ProcurementAuditor
from forms.models.incomplete_construction_work import IncompleteConstructionWork
from forms.models.quarterly_program import QuarterlyProgram
from forms.models.drp_expense import DPRExpense
from forms.models.yearly_target import YearlyTarget
from forms.models.service_flow import ServiceFlow
from forms.models.house_map_construction import HouseMapConstruction
from forms.models.vechile_purches import VehiclePurchase
from forms.models.additionalconvenience import AdditionalConvenience
from forms.models.conditionalgrant import ConditionalGrant
from forms.models.designation_vacancy import DesignationVacancy
from forms.models.contract_desc import ContractDesc
from forms.models.recover_amount import RecoverAmount
from forms.models.expense_desc import ExpenseDesc
from forms.models.integral_advancement import IntegralAdvancement
from forms.models.state_partnership_program import StatePartnershipProgram
from forms.models.teacherdesignation import TeacherDesignation
from forms.models.judicialcommittee import JudicialCommittee
from forms.models.consumercommitteecons_desc import ConsumerCommitteeConstructionDescription
from forms.models.financialstatement import FinancialStatement
from forms.models.budgetsubapproval import BudgetSubmitApproval
from forms.models.procedure_guide import ProcedureGuide
from forms.models.expenditure_exceeding_allocation import ExpenditureExceedingAllocation
from forms.models.sectoral_budget import SectoralBudget
from forms.models.foreign_trip import ForeignTrip
from forms.models.expenditure_detail import ExpenditureDetail
from forms.models.revenue_distribution import RevenueDistribution
from forms.models.state_partnership_program import StatePartnershipProgram

from master_data.models import FiscalYear, Province, District, LocalLevel, GovernmentBody
from users.models.user import User
from collection.utils import COLLECTION_SIX_STATE, STATUS


class CollectionSixFormCollection(models.Model):
    province = models.ForeignKey(
        Province, on_delete=models.PROTECT, null=True, blank=False)
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, null=True, blank=False)
    local_level = models.ForeignKey(
        LocalLevel, on_delete=models.PROTECT, null=True, blank=False)
    body = models.ForeignKey(
        GovernmentBody, on_delete=models.PROTECT, blank=True, null=True)
    fiscal_year = models.ForeignKey(
        FiscalYear, on_delete=models.PROTECT, null=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.IntegerField(
        choices=COLLECTION_SIX_STATE, default=0, blank=True)
    status = models.CharField(choices=STATUS, default='started', max_length=20)
    approver = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True, related_name='collectin_six_approver_user')
    reject_msg = models.CharField(null=True, blank=True, max_length=250)

    procurement_auditor = models.OneToOneField(
        ProcurementAuditor, on_delete=models.PROTECT, null=True, blank=False)
    incomplete_construction_work = models.OneToOneField(
        IncompleteConstructionWork, on_delete=models.PROTECT, null=True, blank=False)
    quarterly_program = models.OneToOneField(
        QuarterlyProgram, on_delete=models.PROTECT, null=True, blank=False)
    dpr_expense = models.OneToOneField(
        DPRExpense, on_delete=models.PROTECT, null=True, blank=False)
    yearly_target = models.OneToOneField(
        YearlyTarget, on_delete=models.PROTECT, null=True, blank=False)
    service_flow = models.OneToOneField(
        ServiceFlow, on_delete=models.PROTECT, null=True, blank=False)
    house_map_construction = models.OneToOneField(
        HouseMapConstruction, on_delete=models.PROTECT, null=True, blank=False)
    vehicle_purchase = models.OneToOneField(
        VehiclePurchase, on_delete=models.PROTECT, null=True, blank=False)
    additional_convenience = models.OneToOneField(
        AdditionalConvenience, on_delete=models.PROTECT, null=True, blank=False)
    conditional_grant = models.OneToOneField(
        ConditionalGrant, on_delete=models.PROTECT, null=True, blank=False)
    designation_vacancy = models.OneToOneField(
        DesignationVacancy, on_delete=models.PROTECT, null=True, blank=False)
    contract_desc = models.OneToOneField(
        ContractDesc, on_delete=models.PROTECT, null=True, blank=False)
    recover_amount = models.OneToOneField(
        RecoverAmount, on_delete=models.PROTECT, null=True, blank=False)
    expense_desc = models.OneToOneField(
        ExpenseDesc, on_delete=models.PROTECT, null=True, blank=False)
    integral_advancement = models.OneToOneField(
        IntegralAdvancement, on_delete=models.PROTECT, null=True, blank=False)
    teacher_designation = models.OneToOneField(
        TeacherDesignation, on_delete=models.PROTECT, null=True, blank=False)
    judicial_committee = models.OneToOneField(
        JudicialCommittee, on_delete=models.PROTECT, null=True, blank=False)
    consumer_committee_construction_description = models.OneToOneField(
        ConsumerCommitteeConstructionDescription, on_delete=models.PROTECT, null=True, blank=False)
    financial_statement = models.OneToOneField(
        FinancialStatement, on_delete=models.PROTECT, null=True, blank=False)
    budget_submit_approval = models.OneToOneField(
        BudgetSubmitApproval, on_delete=models.PROTECT, null=True, blank=False)
    procedure_guide = models.OneToOneField(
        ProcedureGuide, on_delete=models.PROTECT, null=True, blank=False)
    expenditure_exceeding_allocation = models.OneToOneField(
        ExpenditureExceedingAllocation, on_delete=models.PROTECT, null=True, blank=False)
    sectoral_budget = models.OneToOneField(
        SectoralBudget, on_delete=models.PROTECT, null=True, blank=False)
    foreign_trip = models.OneToOneField(
        ForeignTrip, on_delete=models.PROTECT, null=True, blank=False)
    expenditure_detail = models.OneToOneField(
        ExpenditureDetail, on_delete=models.PROTECT, null=True, blank=False)
    revenue_distribution = models.OneToOneField(
        RevenueDistribution, on_delete=models.PROTECT, null=True, blank=False)
    state_partnership_program = models.OneToOneField(
        StatePartnershipProgram, on_delete=models.PROTECT, null=True, blank=False)

    def __str__(self):
        display_name = f"{self.user.body} ({self.get_state_display()})"
        return display_name
