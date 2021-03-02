from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.models import (
    ReliefDistributionExpense,
    ReliefDistributionExpenseLine
)


class ReliefDistributionExpenseLineForm(forms.ModelForm):

    class Meta:
        model = ReliefDistributionExpenseLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


ReliefDistributionExpenseFormSet = inlineformset_factory(
    ReliefDistributionExpense,
    ReliefDistributionExpenseLine,
    form=ReliefDistributionExpenseLineForm,
    fields=[
        'relief_type',
        'amt_expense',
        'num_relif_beneficiary',
        'remarks',
        'relief_distribution'
    ],
    extra=1,
    can_delete=True
)


class ReliefDistributionExpenseForm(forms.ModelForm):

    class Meta:
        model = ReliefDistributionExpense
        exclude = ('create_user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form_to_submit'
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Hidden('next_state', 'next'),
            Row(
                Column('body', css_class='col-md-6 mb-0'),
                Column('fiscal_year', css_class='col-md-6 mb-0'),
                css_class='form-row'
            ),
            Div(
                Fieldset(
                    '',
                    Formset('lines')
                ),
            )
        )
