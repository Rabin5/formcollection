from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, Submit, ButtonHolder

from forms.custom_layout_object import Formset
from forms.models.industry_financial_incentive import IndustryFinancialIncentive, IndustryFinancialIncentiveLine


class IndustryFinancialIncentiveLineForm(forms.ModelForm):

    class Meta:
        model = IndustryFinancialIncentiveLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


IndustryFinancialIncentiveFormSet = inlineformset_factory(
    IndustryFinancialIncentive, IndustryFinancialIncentiveLine, form=IndustryFinancialIncentiveLineForm,
    fields=['fiscal_year', 'industry_name', 'total_job_opening', 'financial_incentive_amount',
            'industryfinancialincentive_line'
            ],
    extra=1,
    can_delete=True
)


class IndustryFinancialIncentiveForm(forms.ModelForm):

    class Meta:
        model = IndustryFinancialIncentive
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
