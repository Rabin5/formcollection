from forms.forms.fund_receipt_expense_forms import FundReceiptExpenseForm
from forms.forms.riskallowance_forms import RiskAllowanceForm
from forms.forms.med_exp_forms import MedExpForm
from forms.forms.medical_receipt import MedicalReceiptForm
from forms.forms.medical_use import MedicalUseForm
from forms.forms.pcr_test import PcrTestForm
from forms.forms.rdt_test import RdtTestForm

from forms import models

from forms.views import (
    fund_receipt_expense_views,
    risk_allowance_views,
    medical_expense_views,
    medical_receipt,
    medical_use,
    pcr_test,
    rdt_test,
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

    'fund_receipt_expense': {
        'title': 'कोभिड-१९ रोकथाम नियन्त्रण र व्यवस्थापनमा प्राप्त रकम र खर्च सम्बन्धी बिबरण',
        'form': FundReceiptExpenseForm,
        'model': models.FundReceiptExpense,
        'form_field': 'fund_receipt_expense',
        'update_view': fund_receipt_expense_views.FundReceiptExpenseUpdateView,
    },
}