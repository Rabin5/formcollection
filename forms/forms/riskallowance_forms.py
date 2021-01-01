from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models.risk_allowance import RiskAllowanceLine, RiskAllowance


class RiskAllowanceLineForm(forms.ModelForm):

    class Meta:
        model = RiskAllowanceLine
        exclude = ()


RiskAllowanceFormSet = inlineformset_factory(
    RiskAllowance, RiskAllowanceLine, form=RiskAllowanceLineForm,
    fields=['body', 'office_bearer',
            'bearer_num', 'allowance_type', 'expense_amount', 'remarks'],
    extra=1,
    can_delete=True
)


class RiskAllowanceForm(forms.ModelForm):

    class Meta:
        model = RiskAllowance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('body'),
                Field('fiscal_year_from'),
                Fieldset('Add lines. . .',
                         Formset('lines')
                         ),
                HTML('<br>'),
                ButtonHolder(Submit('submit', 'save')),
            )
        )
