from crispy_forms.helper import FormHelper
from crispy_forms.layout import (ButtonHolder, Column, Div, Fieldset, Hidden,
                                 Layout, Row, Submit)
from django import forms
from django.forms.models import inlineformset_factory

from forms.custom_layout_object import Formset
from forms.models.cashforwork import CashForWork, CashForWorkLine


class CashForWorkLineForm(forms.ModelForm):
    class Meta:
        model = CashForWorkLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


CashForWorkFormSet = inlineformset_factory(
    CashForWork, CashForWorkLine, form=CashForWorkLineForm,
    fields=['formulated_plans', 'estimated_cost', 'is_included', 'estimated_num_jobs', 'jobs_pre_previous_fy', 'jobs_previous_fy',
            'jobs_current_fy', 'expense_jobs_pre_previous_fy', 'expense_jobs_previous_fy', 'expense_jobs_current_fy',
            ],
    extra=1,
    can_delete=True
)


class CashForWorkForm(forms.ModelForm):

    class Meta:
        model = CashForWork
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
