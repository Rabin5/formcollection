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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


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
        self.helper.layout = Layout(
            Div(
                Fieldset('',Formset('lines')
                         ),
            )
        )
        
        
