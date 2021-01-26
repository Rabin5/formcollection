from forms.forms.fund_receipt_expense_forms import FundReceiptExpenseForm
from forms.forms.riskallowance_forms import RiskAllowanceForm
from forms.forms.med_exp_forms import MedExpForm
from forms.forms.medical_receipt import MedicalReceiptForm
from forms.forms.medical_use import MedicalUseForm
from forms.forms.pcr_test import PcrTestForm
from forms.forms.rdt_test import RdtTestForm
from forms.forms.cov_hos_equipment_forms import CovidHospitalEquipmentForm
from forms.forms.med_purchase_desc_forms import MedPurchaseDescForm
from forms.forms.pcr_lab_detail_forms import PcrLaboratoryDetailForm
from forms.forms.pcr_kit_usage_forms import PcrKitUsageForm
from forms.forms.epidemic_outbreak_preparatory_workline_forms import EpidemicOutbreakPreparatoryWorkForm
from forms.forms.action_plan_implementation_forms import ActionPlanImplementationForm
from forms.forms.case_investigation_tracing_forms import CaseInvestigationTracingForm
from forms import models

from forms.views import (
    fund_receipt_expense_views,
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
    epi_outbreak_workline_views,
    action_plan_views,
    case_investigation_views,
)

# Asign form, model, form collection field to route view name
"""
ROUTE_LINK is a dictionary containing form metadata used for all form collections.
"""
ROUTE_LINK = {
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

    'pcr_test_compliance_detail': {
        'title': 'पीसीआर परीक्षण मापदण्डको पालना सम्बन्धी बिबरण',
        'form': PcrTestForm,
        'model': models.PcrTestComplianceDetail,
        'form_field': 'pcr_test_compliance_detail',
        'update_view': pcr_test.PcrTestUpdateView,
    },

    'rdt_test_detail': {
        'title': 'आरडीटी परीक्षण सम्बन्धी बिबरण',
        'form': RdtTestForm,
        'model': models.RdtTestDetail,
        'form_field': 'rdt_test_detail',
        'update_view': rdt_test.RdtTestUpdateView,
    },
    'med_purchase_desc': {
        'title': 'केही प्रमुख स्वास्थ्य सामाग्रीको खरिद दर सम्बन्धी बिबरण (२०७६।७७)',
        'form': MedPurchaseDescForm,
        'model': models.MedicalPurchaseDescription,
        'form_field': 'med_purchase_desc',
        'update_view': med_purchase_desc_views.MedPurchaseDescUpdateView,
    },

    'pcr_lab_detail': {
        'title': 'पिसीआर प्रयोगशाला  सम्बन्धी बिबरण',
        'form': PcrLaboratoryDetailForm,
        'model': models.PcrLaboratoryDetail,
        'form_field': 'pcr_lab_detail',
        'update_view': pcr_lab_detail_views.PcrLaboratoryDetailUpdateView,
    },

    'pcr_kit_usage': {
        'title': 'पिसीआर किटको उपयोग सम्बन्धी बिबरण',
        'form': PcrKitUsageForm,
        'model': models.PcrKitUsage,
        'form_field': 'pcr_kit_usage',
        'update_view': pcr_kit_usage_views.PcrKitUsageUpdateView,
    },

    # 'cov_hos_equipment': {
    #     'title': 'कोभिड डेडिकेट्ड अस्पतालमा रहेका स्वास्थ्य उपकरण सम्बन्धी विवरण',
    #     'form': CovidHospitalEquipmentForm,
    #     'model': models.CovidHospitalEquipment,
    #     'form_field': 'cov_hos_equipment',
    #     'update_view': cov_hos_equipment_views.CovidHospitalEquipmentUpdateView,
    # },

    'fund_receipt_expense': {
        'title': 'कोभिड-१९ रोकथाम नियन्त्रण र व्यवस्थापनमा प्राप्त रकम र खर्च सम्बन्धी बिबरण',
        'form': FundReceiptExpenseForm,
        'model': models.FundReceiptExpense,
        'form_field': 'fund_receipt_expense',
        'update_view': fund_receipt_expense_views.FundReceiptExpenseUpdateView,
    },
    'epidemic_outbreak_preparatory_work':
    {'title': 'महामारी फैलनसक्ने अबस्थालाई मध्यनजर राख्दै प्रदेश सरकारबाट सम्पादन गरिएको पूर्बतयारी सम्बन्धी कार्य',
     'form': EpidemicOutbreakPreparatoryWorkForm,
     'model': models.EpidemicOutbreakPreparatoryWork,
     'form_field': 'epidemic_outbreak_preparatory_work',
     'update_view': epi_outbreak_workline_views.EpidemicOutbreakWorklineUpdateView,

     },
    'action_plan_implementation':
    {'title': 'महामारी फैलनसक्ने अबस्थालाई मध्यनजर राख्दै प्रदेश सरकारबाट सम्पादन गरिएको कार्य योजना कार्यान्वयन ',
     'form': ActionPlanImplementationForm,
     'model': models.ActionPlanImplementation,
     'form_field': 'action_plan_implementation',
     'update_view': action_plan_views.ActionPlanImplementationUpdateView,

     },
    'case_investigation_tracing':
    {'title': 'केस ईन्भेष्टीगेशन तथा कन्ट्रय्याक्ट ट्रेसिङ्ग',
     'form': CaseInvestigationTracingForm,
     'model': models.CaseInvestigationTracing,
     'form_field': 'case_investigation_tracing',
     'update_view': case_investigation_views.CaseInvestigationTracingUpdateView,
     },

}
