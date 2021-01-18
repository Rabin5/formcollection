
from forms.forms.riskallowance_forms import RiskAllowanceForm, RiskAllowanceLineFormSet
from forms.forms.med_exp_forms import MedExpForm, MedExpLineFormSet
from forms.models import MedicalExpense, RiskAllowance
from forms.views import risk_allowance_views, medical_expense_views


# Asign form, model, form collection field to route view name
"""
ROUTE_LINK is a dictionary containing form metadata used for all form collections.
"""
ROUTE_LINK = {
    'risk_forms': {
        'form': RiskAllowanceForm,
        'lines_set': RiskAllowanceLineFormSet,
        'model': RiskAllowance,
        'form_field': 'risk_allowance',
        'create_view': risk_allowance_views.RiskAllowanceCreateView,
        'update_view': risk_allowance_views.RiskAllowanceUpdateView,
    },
    'med_forms': {
        'form': MedExpForm,
        'lines_set': MedExpLineFormSet,
        'model': MedicalExpense,
        'form_field': 'med_exp',
        'create_view': medical_expense_views.MedExpCreateView,
        'update_view': medical_expense_views.MedExpUpdateView,
    },
}