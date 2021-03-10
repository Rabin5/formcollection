from forms.forms.covid_hos_mainpower import CovidHospitalManpowerForm
from forms.forms.covidhospitaldetail import CovidHospitalDetailForm
from forms.forms.fund_receipt_expense_forms import FundReceiptExpenseForm
from forms.forms.isolationconstructionexpenditure import \
    IsolationConstructionExependitureForm
from forms.forms.isolationmanagementdetail import IsolationManagementDetailForm
from forms.forms.med_exp_forms import MedExpForm
from forms.forms.medical_receipt import MedicalReceiptForm
from forms.forms.medical_use import MedicalUseForm
from forms.forms.pcr_test import PcrTestForm
from forms.forms.quarantine_management_detail_forms import (
    QuarantineManagementDetailForm
)
from forms.forms.rdt_test import RdtTestForm
from forms.forms.riskallowance_forms import RiskAllowanceForm
from forms.forms.cov_hos_equipment_forms import CovidHospitalEquipmentForm
from forms.forms.med_purchase_desc_forms import MedPurchaseDescForm
from forms.forms.pcr_lab_detail_forms import PcrLaboratoryDetailForm
from forms.forms.pcr_kit_usage_forms import PcrKitUsageForm
from forms.forms.quarantine_construction_expenditure_forms import (
    QuarantineConstructionExpenditureForm
)
from forms.forms.epidemic_outbreak_preparatory_workline_forms import (
    EpidemicOutbreakPreparatoryWorkForm
)
from forms.forms.cov_hos_management_checklist_forms import (
    CovidHospitalManagementChecklistForm
)
from forms.forms.districtcovid_management import DistrictCovidManagementForm
from forms.forms.action_plan_implementation_forms import (
    ActionPlanImplementationForm
)
from forms.forms.province_institution_management_forms import (
    ProvinceInstitutionManagementForm
)
from forms.forms.fund_operation_forms import FundOperationForm
from forms.forms.case_investigation_tracing_forms import (
    CaseInvestigationTracingForm
)
from forms.forms.case_invs_tracing_opt import CaseInvestigationTracingOptForm
from forms.forms.reliefprocurementdetail import ReliefProcurementDetailForm
from forms.forms.relief_procure_dist import ReliefProcureDistributionForm
from forms.forms.ward_relief_forms import WardReliefProcureDistributionForm
from forms.forms.received_relief_forms import ReceivedReliefDetailForm
from forms.forms.relief_distribution_forms import ReliefDistributionExpenseForm
from forms.forms.procurement_auditor import ProcurementAuditorForm
from forms.forms.incomplete_construction_work import IncompleteConstructionWorkForm
from forms.forms.quarterly_program import QuarterlyProgramForm
from forms.forms.drp_expense import DPRExpenseForm
from forms.forms.yearly_target import YearlyTargetForm
from forms.forms.service_flow import ServiceFlowFormLine
from forms.forms.house_map_construction import HouseMapConstructionForm
from forms.forms.vechile_purches import VehiclePurchaseFormLine
from forms.forms.additionalconvenience import AdditionalConvenienceFormLine
from forms.forms.conditionalgrant import ConditionalGrantFormLine
from forms.forms.designation_vacancy import DesignationVacancyForm
from forms.forms.conditionalgrant import ConditionalGrantFormLine
from forms.forms.designation_vacancy import DesignationVacancyForm
from forms.forms.contract_desc import ContractDescForm
from forms.forms.recover_amount import RecoverAmountForm
from forms.forms.expense_desc import ExpenseDescForm
from forms.forms.integral_advancement import IntegralAdvancementForm
from forms.forms.teacherdesgination import TeacherDesginationLineForm
from forms.forms.judicialcommittee import JudicialCommitteeFormLine
from forms.forms.consumercommitteecons_desc import ConsumercomConsDespFormLine
from forms.forms.financialstatement import FinancialStatementForm
from forms.forms.budgetsubapproval import BudgetSubmitApprovalFormLine
from forms.forms.procedure_guide import ProcedureGuideForm
from forms.forms.expenditure_exceeding_allocation import ExpenditureExceedingAllocationForm
from forms.forms.sectoral_budget import SectoralBudgetForm
from forms.forms.foreign_trip import ForeignTripForm
from forms.forms.expenditure_detail import ExpenditureDetailForm
from forms.forms.revenue_distribution import RevenueDistributionForm
from forms.forms.state_partnership_program import StatePartnershipProgramForm
from forms import models

from forms.views import (
    fund_receipt_expense_views, quarantine_management_detail_views,
    risk_allowance_views,
    medical_expense_views,
    medical_receipt,
    medical_use,
    pcr_test,
    rdt_test,
    cov_hos_equipment_views,
    med_purchase_desc_views,
    pcr_kit_usage_views,
    pcr_lab_detail_views,
    quarantine_construct_expenditure_views,
    covid_hos_mainpower,
    covidhospitaldetail,
    isolationmanagementdetail,
    isolationconsexpenditure,
    epi_outbreak_workline_views,
    cov_hos_management_checklist_views,
    district_covid_management,
    action_plan_views,
    province_institution_management_views,
    fund_operation_views,
    case_invs_tracing_opt,
    case_investigation_views,
    relief_procure_dist,
    reliefprocurementdetail,
    relief_distribution_views,
    received_relief_views,
    ward_relief_views,

    procurement_auditor_views,
    incomplete_construction_work_views,
    quarterly_program_views,
    drp_expense_views,
    yearly_target_views,
    service_flow,
    house_map_construction,
    vechile_purches,
    additionalconvenience,
    conditionalgrant,
    designation_vacancy_views,
    contract_desc_views,
    recover_amount_views,
    expense_desc_views,
    integral_advancement_views,
    teacherdesignation_view,
    judicialcommittee_view,
    consumercommitteecons_desc_view,
    financialstatement_view,
    budgetsubapproval_view,
    procedure_guide_views,
    expenditure_exceeding_allocation_views,
    sectoral_budget_views,
    foreign_trip_views,
    expenditure_detail_views,
    revenue_distribution_views,
    state_partnership_program_views,
)

# Asign form, model, form collection field to route view name
"""
ROUTE_LINK is a dictionary containing form metadata used for all form \
    collections.
"""
ROUTE_LINK = {
    'fund_receipt_expense': {
        'title': 'कोभिड-१९ रोकथाम नियन्त्रण र व्यवस्थापनमा प्राप्त रकम र खर्च \
            सम्बन्धी बिबरण',
        'form': FundReceiptExpenseForm,
        'model': models.FundReceiptExpense,
        'form_field': 'fund_receipt_expense',
        'update_view': fund_receipt_expense_views.FundReceiptExpenseUpdateView,
    },

    'risk_allowance': {
        'title': 'जोखिम भत्ता सम्बन्धी बिबरण',
        'form': RiskAllowanceForm,
        'model': models.RiskAllowance,
        'form_field': 'risk_allowance',
        'update_view': risk_allowance_views.RiskAllowanceUpdateView,
    },

    'medical_expense': {
        'title': 'औषधी स्वास्थ्य सामग्री एवं उपकरण खरिद',
        'form': MedExpForm,
        'model': models.MedicalExpense,
        'form_field': 'medical_expense',
        'update_view': medical_expense_views.MedExpUpdateView,
    },

    'medical_receipt': {
        'title': 'औषधी स्वास्थ्य सामग्री एवं उपकरण प्राप्ति',
        'form': MedicalReceiptForm,
        'model': models.MedicalReceipt,
        'form_field': 'medical_receipt',
        'update_view': medical_receipt.MedicalReceiptUpdateView,
    },

    'medical_use': {
        'title': 'औषधी, स्वास्थ्य सामग्री एवं उपकरणको उपयोग',
        'form': MedicalUseForm,
        'model': models.MedicalUse,
        'form_field': 'medical_use',
        'update_view': medical_use.MedicalUseUpdateView,
    },

    'med_purchase_desc': {
        'title': 'केही प्रमुख स्वास्थ्य सामाग्रीको खरिद दर सम्बन्धी बिबरण \
            (२०७६।७७)',
        'form': MedPurchaseDescForm,
        'model': models.MedicalPurchaseDescription,
        'form_field': 'med_purchase_desc',
        'update_view': med_purchase_desc_views.MedPurchaseDescUpdateView,
    },

    'pcr_test_compliance_detail': {
        'title': 'पीसीआर परीक्षण मापदण्डको पालना सम्बन्धी बिबरण',
        'form': PcrTestForm,
        'model': models.PcrTestComplianceDetail,
        'form_field': 'pcr_test_compliance_detail',
        'update_view': pcr_test.PcrTestUpdateView,
    },

    'pcr_lab_detail': {
        'title': 'पिसीआर प्रयोगशाला सम्बन्धी बिबरण',
        'form': PcrLaboratoryDetailForm,
        'model': models.PcrLaboratoryDetail,
        'form_field': 'pcr_lab_detail',
        'update_view': pcr_lab_detail_views.PcrLaboratoryDetailUpdateView,
    },

    'rdt_test_detail': {
        'title': 'आरडीटी परीक्षण सम्बन्धी बिबरण',
        'form': RdtTestForm,
        'model': models.RdtTestDetail,
        'form_field': 'rdt_test_detail',
        'update_view': rdt_test.RdtTestUpdateView,
    },

    'pcr_kit_usage': {
        'title': 'पिसीआर किटको उपयोग सम्बन्धी बिबरण',
        'form': PcrKitUsageForm,
        'model': models.PcrKitUsage,
        'form_field': 'pcr_kit_usage',
        'update_view': pcr_kit_usage_views.PcrKitUsageUpdateView,
    },

    'covid_hos_mainpower': {
        'title': 'कोभिड डेडिकेट्ड अस्पतालमा रहेका स्वास्थ्य जनशक्ति सम्बन्धी \
            विवरण',
        'form': CovidHospitalManpowerForm,
        'model': models.CovidHospitalManpower,
        'form_field': 'covid_hos_mainpower',
        'update_view': covid_hos_mainpower.CovidHospitalMainpowerUpdateView,
    },

    'cov_hos_equipment': {
        'title': 'कोभिड डेडिकेट्ड अस्पतालमा रहेका स्वास्थ्य उपकरण सम्बन्धी \
            विवरण',
        'form': CovidHospitalEquipmentForm,
        'model': models.CovidHospitalEquipment,
        'form_field': 'cov_hos_equipment',
        'update_view': cov_hos_equipment_views.
        CovidHospitalEquipmentUpdateView,
    },

    'covid_hospital_detail': {
        'title': 'कोभिड अस्पताल सम्बन्धी बिबरण (कोभिड अस्पतालको विवरण उल्लेख \
            गर्ने )',
        'form': CovidHospitalDetailForm,
        'model': models.CovidHospitalDetail,
        'form_field': 'covid_hospital_detail',
        'update_view': covidhospitaldetail.CovidHospitalDetailUpdateView,
    },

    'quarantine_management_detail': {
        'title': 'क्वारेन्टीन व्यवस्थापन सम्बन्धी बिबरण',
        'form': QuarantineManagementDetailForm,
        'model': models.QuarantineManagementDetail,
        'form_field': 'quarantine_management_detail',
        'update_view': quarantine_management_detail_views.
        QuarantineManagementDetailUpdateView,
    },

    'isolation_management_detail': {
        'title': 'आसोलेशनकेन्द्र व्यवस्थापन सम्बन्धी बिबरण ',
        'form': IsolationManagementDetailForm,
        'model': models.IsolationManagementDetail,
        'form_field': 'isolation_management_detail',
        'update_view': isolationmanagementdetail.
        IsolationdetailMangementUpdateView,
    },

    'quarantine_contruction_expenditure': {
        'title': 'क्वारेन्टीन निर्माणमा खरिद भएका सामग्री र खर्च रकम एवं खरिद \
            प्रकृया',
        'form': QuarantineConstructionExpenditureForm,
        'model': models.QuarantineConstructionExpenditure,
        'form_field': 'quarantine_contruction_expenditure',
        'update_view': quarantine_construct_expenditure_views.
        QuarantineConstructionExpenditureUpdateView,
    },

    'isolation_construction_expenditure': {
        'title': 'आइसोलेशन निर्माणमा खरिद भएका सामग्री र खर्च रकम एवं खरिद \
            प्रकृया ',
        'form': IsolationConstructionExependitureForm,
        'model': models.IsolationConstructionExependiture,
        'form_field': 'isolation_construction_expenditure',
        'update_view': isolationconsexpenditure.
        IsolationConsExpenditureUpdateView,
    },

    'cov_hos_management_checklist': {
        'title': 'कोभिड अस्पताल ब्यबस्थापन सम्बन्धी चेकलिष्ट',
        'form': CovidHospitalManagementChecklistForm,
        'model': models.CovidHospitalManagementChecklist,
        'form_field': 'cov_hos_management_checklist',
        'update_view': cov_hos_management_checklist_views.
        CovidHospitalManagementChecklistUpdateView,
    },

    'epidemic_outbreak_prep': {
        'title': 'महामारी फैलनसक्ने अबस्थालाई मध्यनजर राख्दै प्रदेश सरकारबाट \
            सम्पादन गरिएको पूर्बतयारी सम्बन्धी कार्य',
        'form': EpidemicOutbreakPreparatoryWorkForm,
        'model': models.EpidemicOutbreakPreparatoryWork,
        'form_field': 'epidemic_outbreak_prep',
        'update_view': epi_outbreak_workline_views.
        EpidemicOutbreakWorklineUpdateView,
    },

    'district_covid_management': {
        'title': 'प्रदेश अन्तर्गत कोभिड-१९ को पहिचान, परीक्षण र उपचार एवं \
            पूर्वाधार सम्बन्धी जिल्लागत विवरण (२०७७ आषाढ मसान्त सम्म)',
        'form': DistrictCovidManagementForm,
        'model': models.DistrictCovidManagement,
        'form_field': 'district_covid_management',
        'update_view': district_covid_management.
        DistrictCovidManagementUpdateView,
    },

    'action_plan_implementation': {
        'title': 'कार्ययोजना कार्यान्वयन- कोभिड-१९ को विश्वव्यापी संक्रमणको \
            कारणबाट उत्पन्न असहज परिस्थितिमा स्वदेश आउनैपर्ने अवस्थामा रहेका \
                नेपाली नागरिकलाई स्वदेश आउन सहजीकरण गर्ने सम्वन्धी आदेश, २०७७ \
                    को लागि तयार पारिएको नेपाली नागरिकलाई स्वदेश आउन सहजीकरण \
                        गर्ने सम्बन्धी कार्ययोजना २०७७ बमोजिम देहायका \
                            कार्यहरु अन्य सरकारी निकायको साथै प्रदेश सरकारको \
                                समेत जिम्मेवारी हुने सहयोग गर्नुपर्ने गरी \
                                    तोकेको छ । यस सम्बन्धमा प्रदेश सरकारबाट \
                                        भएका क्रियाकलाप र यसमा भएको खर्च \
                                            खुलाउनु होस् ।',
        'form': ActionPlanImplementationForm,
        'model': models.ActionPlanImplementation,
        'form_field': 'action_plan_implementation',
        'update_view': action_plan_views.ActionPlanImplementationUpdateView,
    },

    'province_institute_management': {
        'title': 'संस्थागत व्यवस्था- कोभिड-१९ को रोकथाम, नियन्त्रण तथा \
            व्यवस्थापनमा प्रदेश सरकारको भूमिका महत्वपूर्ण रहँदै आएको छ । \
                उल्लिखित भूमिका निर्वाहको लागि तहमा प्रदेश सरकार अन्तर्गत गठन \
                    भएको PCCMC लगायतका संस्थागत व्यवस्था र ती संरचनबाट \
                        सम्पादित कार्यको सम्बन्धमा उल्लेख गर्नुहोस् ।',
        'form': ProvinceInstitutionManagementForm,
        'model': models.ProvinceInstitutionManagement,
        'form_field': 'province_institute_management',
        'update_view': province_institution_management_views.
        ProvinceInstitutionManagementUpdateView,
    },

    'fund_operation': {
        'title': 'कोष सञ्चालन',
        'form': FundOperationForm,
        'model': models.FundOperation,
        'form_field': 'fund_operation',
        'update_view': fund_operation_views.FundOperationUpdateView,
    },

    'case_investigation_tracing': {
        'title': 'केस ईन्भेष्टीगेशन तथा कन्ट्रय्याक्ट ट्रेसिङ्ग २०७६।७७',
        'form': CaseInvestigationTracingForm,
        'model': models.CaseInvestigationTracing,
        'form_field': 'case_investigation_tracing',
        'update_view': case_investigation_views.
        CaseInvestigationTracingUpdateView,
    },

    'case_investigation_tracing_operation': {
        'title': 'केश अनुसन्धान तथा कन्याक्ट खोजपड्ताल टीम  परिचालन',
        'form': CaseInvestigationTracingOptForm,
        'model': models.CaseInvestigationTracingOperations,
        'form_field': 'case_investigation_tracing_operation',
        'update_view': case_invs_tracing_opt.CaseInvTacingOptUpdateView,
    },

    'relief_procurement_detail': {
        'title': 'राहत सामग्री खरिद विधिसम्बन्धी विवरण',
        'form': ReliefProcurementDetailForm,
        'model': models.ReliefProcurementDetail,
        'form_field': 'relief_procurement_detail',
        'update_view': reliefprocurementdetail.
        ReliefProcurementDetailUpdateView,
    },

    'relief_procurement_distribution': {
        'title': ' राहात सामग्रीको खरिद र वितरणको परिमाण',
        'form': ReliefProcureDistributionForm,
        'model': models.ReliefProcureDistribution,
        'form_field': 'relief_procurement_distribution',
        'update_view': relief_procure_dist.ReliefProcureDistributionUpdateView,
    },

    'ward_relief_procurement_dist': {
        'title': 'वडा अनुसारको राहात सामग्री खरिद र वितरणको विवरण',
        'form': WardReliefProcureDistributionForm,
        'model': models.WardReliefProcureDistribution,
        'form_field': 'ward_relief_procurement_dist',
        'update_view': ward_relief_views.
        WardReliefProcureDistributionUpdateView,
    },

    'received_relief_detail': {
        'title': ' संघ संस्था तथा व्यक्तीबाट राहत वितरणको लागि प्राप्त उपभोग्य \
            वस्तुहरुको परिमाण र वितरण',
        'form': ReceivedReliefDetailForm,
        'model': models.ReceivedReliefDetail,
        'form_field': 'received_relief_detail',
        'update_view': received_relief_views.ReceivedReliefDetailUpdateView,
    },

    'relief_distribution_expense': {
        'title': 'राहत वितरण खर्च सम्वन्धी विवरण',
        'form': ReliefDistributionExpenseForm,
        'model': models.ReliefDistributionExpense,
        'form_field': 'relief_distribution_expense',
        'update_view': relief_distribution_views.
        ReliefDistributionExpenseUpdateView,
    },
    'procurement_auditor': {
        'title': 'बोलपत्र, सिलबन्दी दरभाउपत्र बेगर काम टुक्रा पारी खरिद गरेको विवरण',
        'form': ProcurementAuditorForm,
        'model': models.ProcurementAuditor,
        'form_field': 'procurement_auditor',
        'update_view': procurement_auditor_views.ProcurementAuditorUpdateView,
    },
    'incomplete_construction_work': {
        'title': 'अधुरो निर्माण कार्यको विवरण',
        'form': IncompleteConstructionWorkForm,
        'model': models.IncompleteConstructionWork,
        'form_field': 'incomplete_construction_work',
        'update_view': incomplete_construction_work_views.IncompleteConstructionWorkUpdateView,
    },
    'quarterly_program': {
        'title': 'चौमासिक कार्यक्रम सञ्चालन÷पुँजीगत खर्च विवरण',
        'form': QuarterlyProgramForm,
        'model': models.QuarterlyProgram,
        'form_field': 'quarterly_program',
        'update_view': quarterly_program_views.QuarterlyProgramUpdateView},
    'dpr_expense': {
        'title': 'डिपिआर खर्च सम्बन्धी विवरण',
        'form': DPRExpenseForm,
        'model': models.DPRExpense,
        'form_field': 'dpr_expense',
        'update_view': drp_expense_views.DPRExpenseUpdateView,
    },
    'yearly_target': {
        'title': 'वार्षिक लक्ष्य तथा प्रगति',
        'form': YearlyTargetForm,
        'model': models.YearlyTarget,
        'form_field': 'yearly_target',
        'update_view': yearly_target_views.YearlyTargetUpdateView,
    },
    'service_flow': {
        'title': 'सेवा प्रवाह सम्वन्धी विवरण (स्थानीय तहको लागि)',
        'form': ServiceFlowFormLine,
        'model': models.ServiceFlow,
        'form_field': 'service_flow',
        'update_view': service_flow.ServiceFlowUpdateView,
    },
    'house_map_construction': {
        'title': 'घर नक्शापास र निर्माण कार्य सम्पन्न सम्वन्धी विवरण (स्थानीय तहको लागि)',
        'form': HouseMapConstructionForm,
        'model': models.HouseMapConstruction,
        'form_field': 'house_map_construction',
        'update_view': house_map_construction.HouseMapConstructionUpdateView,
    },
    'vehicle_purchase': {
        'title': 'सवारी साधन खरिदको विवरण (स्थानीय तहको लागि)',
        'form': VehiclePurchaseFormLine,
        'model': models.VehiclePurchase,
        'form_field': 'vehicle_purchase',
        'update_view': vechile_purches.VehiclePurchaseUpdateView,
    },
    'additional_convenience': {
        'title': 'थप सुविधाको विवरण (स्थानीय तह र प्रदेश तहको लागि)',
        'form': AdditionalConvenienceFormLine,
        'model': models.AdditionalConvenience,
        'form_field': 'additional_convenience',
        'update_view': additionalconvenience.AdditionalConvenienceUpdateView,
    },
    'conditional_grant': {
        'title': 'सशर्त अनुदानतर्फ रकम फ्रिजको विवरण (स्थानीय तहको लागि)',
        'form': ConditionalGrantFormLine,
        'model': models.ConditionalGrant,
        'form_field': 'conditional_grant',
        'update_view': conditionalgrant.ConditionalGrantUpdateView,
    },
    'designation_vacancy': {
        'title': 'दरवन्दी र पदपूर्तिको विवरण(स्थानीय तह र प्रदेश तहको लागि)',
        'form': DesignationVacancyForm,
        'model': models.DesignationVacancy,
        'form_field': 'designation_vacancy',
        'update_view': designation_vacancy_views.DesignationVacancyUpdateView,
    },
    'contract_desc': {
        'title': 'कर, दस्तुर, सेवा शुल्क र भाडाको ठेक्का सम्बन्धी विवरण',
        'form': ContractDescForm,
        'model': models.ContractDesc,
        'form_field': 'contract_desc',
        'update_view': contract_desc_views.ContractDescUpdateView,
    },
    'recover_amount': {
        'title': 'असुल गर्न बाँकी बक्यौता सम्बन्धी विवरण',
        'form': RecoverAmountForm,
        'model': models.RecoverAmount,
        'form_field': 'recover_amount',
        'update_view': recover_amount_views.RecoverAmountUpdateView,
    },
    'expense_desc': {
        'title': 'आर्थिक सहायता, भैपरी आउने र प्रशासनिक खर्चको विवरण',
        'form': ExpenseDescForm,
        'model': models.ExpenseDesc,
        'form_field': 'expense_desc',
        'update_view': expense_desc_views.ExpenseDescUpdateView,
    },
    'integral_advancement': {
        'title': 'आ.व २०७६।७७ सम्मको पेश्कीको एकीकृत विवरण',
        'form': IntegralAdvancementForm,
        'model': models.IntegralAdvancement,
        'form_field': 'integral_advancement',
        'update_view': integral_advancement_views.IntegralAdvancementUpdateView,
    },
    'teacher_designation': {
        'title': 'शिक्षक दरबन्दी र पदपूर्ति विवरण',
        'form': TeacherDesginationLineForm,
        'model': models.teacherdesignation.TeacherDesignation,
        'form_field': 'teacher_designation',
        'update_view': teacherdesignation_view.TeacherDesginationUpdateView,
    },
    'judicial_committee': {
        'title': 'न्यायीक समिती (उजुरी र फछयौट) विवरण',
        'form': JudicialCommitteeFormLine,
        'model': models.judicialcommittee.JudicialCommittee,
        'form_field': 'judicial_committee',
        'update_view': judicialcommittee_view.JudicialCommitteeUpdateView,
    },
    'consumer_committee_construction_description': {
        'title': ' कुल निर्माण कार्य मध्ये उपभोक्ता समिती र निर्माण व्यवसायीबाट भएको कार्य सम्बन्धि विवरण',
        'form': ConsumercomConsDespFormLine,
        'model': models.consumercommitteecons_desc.ConsumerCommitteeConstructionDescription,
        'form_field': 'consumer_committee_construction_description',
        'update_view': consumercommitteecons_desc_view.ConsumercomConsDespUpdateView,
    },
    'financial_statement': {
        'title': ' सुत्रबाट प्राप्त हुने वित्तीय विवरण र अनुसूचीबाट देखिएका व्यहोरा सम्बन्धी विवरण',
        'form': FinancialStatementForm,
        'model': models.financialstatement.FinancialStatement,
        'form_field': 'financial_statement',
        'update_view': financialstatement_view.Financial_St_ResUpdateView,
    },
    'budget_submit_approval': {
        'title': 'बजेट पेश र स्वीकृति',
        'form': BudgetSubmitApprovalFormLine,
        'model': models.budgetsubapproval.BudgetSubmitApproval,
        'form_field': 'budget_submit_approval',
        'update_view': budgetsubapproval_view.BudgetSubmitApprovalUpdateView,
    },
    'procedure_guide': {
        'title': 'कानून कार्यविधि निर्देशिका एवं नर्म्स तयारी सम्बन्धी विवरण',
        'form': ProcedureGuideForm,
        'model': models.ProcedureGuide,
        'form_field': 'procedure_guide',
        'update_view': procedure_guide_views.ProcedureGuideUpdateView,
    },
    'expenditure_exceeding_allocation': {
        'title': 'विनियोजनभन्दा बढी खर्च सम्बन्धी विवरण',
        'form': ExpenditureExceedingAllocationForm,
        'model': models.ExpenditureExceedingAllocation,
        'form_field': 'expenditure_exceeding_allocation',
        'update_view': expenditure_exceeding_allocation_views.ExpenditureExceedingAllocationUpdateView,
    },
    'sectoral_budget': {
        'title': ' क्षेत्रगत बजेट र खर्च सम्बन्धी विवरण',
        'form': SectoralBudgetForm,
        'model': models.SectoralBudget,
        'form_field': 'sectoral_budget',
        'update_view': sectoral_budget_views.SectoralBudgetUpdateView,
    },
    'foreign_trip': {
        'title': 'बैदेशिक भ्रमण सम्बन्धी विवरण',
        'form': ForeignTripForm,
        'model': models.ForeignTrip,
        'form_field': 'foreign_trip',
        'update_view': foreign_trip_views.ForeignTripUpdateView,
    },
    'expenditure_detail': {
        'title': 'अनुदान प्राप्ति, खर्च र बाँकीको विवरण',
        'form': ExpenditureDetailForm,
        'model': models.ExpenditureDetail,
        'form_field': 'expenditure_detail',
        'update_view': expenditure_detail_views.ExpenditureDetailUpdateView,
    },
    'revenue_distribution': {
        'title': 'राजश्व बाँडफाँड सम्बन्धी विवरण',
        'form': RevenueDistributionForm,
        'model': models.RevenueDistribution,
        'form_field': 'revenue_distribution',
        'update_view': expenditure_detail_views.ExpenditureDetailUpdateView,
    },
    'state_partnership_program': {
        'title': ' प्रदेश र स्यानीय पूर्वाधार विकास साझेदारी कार्यक्रम सम्बन्धी विवरण',
        'form': StatePartnershipProgramForm,
        'model': models.StatePartnershipProgram,
        'form_field': 'state_partnership_program',
        'update_view': state_partnership_program_views.StatePartnershipProgramtUpdateView,
    },


}
