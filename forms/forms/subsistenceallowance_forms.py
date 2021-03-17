from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, Submit, ButtonHolder

from forms.custom_layout_object import Formset
from forms.models.subsistenceallowance import SubsistenceAllowance, SubsistenceAllowanceLine


class SubsistenceAllowanceLineForm(forms.ModelForm):

    class Meta:
        model = SubsistenceAllowanceLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


SubsistenceAllowanceFormSet = inlineformset_factory(
    SubsistenceAllowance, SubsistenceAllowanceLine, form=SubsistenceAllowanceLineForm,
    fields=['fiscal_year', 'total_unemployed_families', 'subsistence_allowance_amount', 'subsistenceallowance_line'
            ],
    extra=1,
    can_delete=True
)


class SubsistenceAllowanceForm(forms.ModelForm):

    class Meta:
        model = SubsistenceAllowance
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
