from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, Submit, ButtonHolder

from forms.custom_layout_object import Formset
from forms.models.financialassistanceline import FinancialAssistance, FinancialAssistanceLine


class FinancialAssistanceLineForm(forms.ModelForm):

    class Meta:
        model = FinancialAssistanceLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


FinancialAssistanceFormSet = inlineformset_factory(
    FinancialAssistance, FinancialAssistanceLine, form=FinancialAssistanceLineForm,
    fields=['fiscal_year', 'foreign_employment_board_received_amount', 'concerned_distribution_amount',
            'financialassistance_line'
            ],
    extra=1,
    can_delete=True
)


class FinancialAssistanceForm(forms.ModelForm):

    class Meta:
        model = FinancialAssistance
        exclude = ('create_user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form_to_submit'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Hidden('next_state', 'next'),
            Row(
                css_class='form-row'
            ),
            Div(
                Fieldset('',
                         Formset('lines')
                         ),
                ButtonHolder(Submit('submit', 'save')),
            )
        )
