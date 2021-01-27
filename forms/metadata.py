from forms.forms.covid_hos_mainpower import CovidHospitalManpowerForm
from forms.forms.covidhospitaldetail import CovidHospitalDetailForm
from forms.forms.quarantine_management_detail_forms import QuarantineManagementDetailForm
from forms.forms.fund_receipt_expense_forms import FundReceiptExpenseForm
from forms.forms.isolationconstructionexpenditure import \
    IsolationConstructionExependitureForm
from forms.forms.isolationmanagementdetail import IsolationManagementDetailForm
from forms.forms.med_exp_forms import MedExpForm
from forms.forms.medical_receipt import MedicalReceiptForm
from forms.forms.medical_use import MedicalUseForm
from forms.forms.pcr_test import PcrTestForm
from forms.forms.rdt_test import RdtTestForm
from forms.forms.riskallowance_forms import RiskAllowanceForm
from forms.forms.cov_hos_equipment_forms import CovidHospitalEquipmentForm
from forms.forms.med_purchase_desc_forms import MedPurchaseDescForm
from forms.forms.pcr_lab_detail_forms import PcrLaboratoryDetailForm
from forms.forms.pcr_kit_usage_forms import PcrKitUsageForm
from forms.forms.quarantine_construction_expenditure_forms import QuarantineConstructionExpenditureForm
from forms.forms.cov_hos_management_checklist_forms import CovidHospitalManagementChecklistForm
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
    cov_hos_management_checklist_views,
    covid_hos_mainpower,
    covidhospitaldetail,
    isolationmanagementdetail,
    isolationconsexpenditure,
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

    'cov_hos_equipment': {
        'title': 'कोभिड डेडिकेट्ड अस्पतालमा रहेका स्वास्थ्य उपकरण सम्बन्धी विवरण',
        'form': CovidHospitalEquipmentForm,
        'model': models.CovidHospitalEquipment,
        'form_field': 'cov_hos_equipment',
        'update_view': cov_hos_equipment_views.CovidHospitalEquipmentUpdateView,
    },

    'fund_receipt_expense': {
        'title': 'कोभिड-१९ रोकथाम नियन्त्रण र व्यवस्थापनमा प्राप्त रकम र खर्च सम्बन्धी बिबरण',
        'form': FundReceiptExpenseForm,
        'model': models.FundReceiptExpense,
        'form_field': 'fund_receipt_expense',
        'update_view': fund_receipt_expense_views.FundReceiptExpenseUpdateView,
    },


    'covid_hos_mainpower': {
        'title': 'कोभिड डेडिकेट्ड अस्पतालमा रहेका स्वास्थ्य जनशक्ति सम्बन्धी विवरण ',
        'form': CovidHospitalManpowerForm,
        'model': models.CovidHospitalManpower,
        'form_field': 'covid_hos_mainpower',
        'update_view': covid_hos_mainpower.CovidHospitalMainpowerUpdateView,
    },
    'covid_hospital_detail': {
        'title': 'कोभिड अस्पताल सम्बन्धी बिबरण',
        'form': CovidHospitalDetailForm,
        'model': models.CovidHospitalDetail,
        'form_field': 'covid_hospital_detail',
        'update_view': covidhospitaldetail.CovidHospitalDetailUpdateView,
    },
    'isolation_management_detail': {
        'title': 'आसोलेशनकेन्द्र व्यवस्थापन सम्बन्धी बिबरण ',
        'form': IsolationManagementDetailForm,
        'model': models.IsolationManagementDetail,
        'form_field': 'isolation_management_detail',
        'update_view': isolationmanagementdetail.IsolationdetailMangementUpdateView,
    },
    'isolation_construction_expenditure': {
        'title': 'आइसोलेशन निर्माणमा खरिद भएका सामग्री र खर्च रकम एवं खरिद प्रकृया ',
        'form': IsolationConstructionExependitureForm,
        'model': models.IsolationConstructionExependiture,
        'form_field': 'isolation_construction_expenditure',
        'update_view': isolationconsexpenditure.IsolationConsExpenditureUpdateView,
    },
    'quarantine_management_detail': {
        'title': 'क्वारेन्टीन व्यवस्थापन सम्बन्धी बिबरण',
        'form': QuarantineManagementDetailForm,
        'model': models.QuarantineManagementDetail,
        'form_field': 'quarantine_management_detail',
        'update_view': quarantine_management_detail_views.QuarantineManagementDetailUpdateView,
    },
    'quarantine_contruction_expenditure': {
        'title': 'क्वारेन्टीन निर्माणमा खरिद भएका सामग्री र खर्च रकम एवं खरिद प्रकृया',
        'form': QuarantineConstructionExpenditureForm,
        'model': models.QuarantineConstructionExpenditure,
        'form_field': 'quarantine_contruction_expenditure',
        'update_view': quarantine_construct_expenditure_views.QuarantineConstructionExpenditureUpdateView,
    },
    'cov_hos_management_checklist': {
        'title': 'कोभिड अस्पताल ब्यबस्थापन सम्बन्धी चेकलिष्ट',
        'form': CovidHospitalManagementChecklistForm,
        'model': models.CovidHospitalManagementChecklist,
        'form_field': 'cov_hos_management_checklist',
        'update_view': cov_hos_management_checklist_views.CovidHospitalManagementChecklistUpdateView,
    },

}
