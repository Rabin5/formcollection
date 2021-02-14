from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.models import FundReceiptExpense, FundReceiptExpenseLine
from master_data.widgets import NepaliDateInput

class FundReceiptExpenseLineForm(forms.ModelForm):

    class Meta:
        model = FundReceiptExpenseLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
            


FundReceiptExpenseLineFormset = inlineformset_factory(
    FundReceiptExpense, FundReceiptExpenseLine, form=FundReceiptExpenseLineForm,
    fields=['budget_source', 'fy_start_received_amt', 'fy_end_received_amt', 'expense_header', 'fy_start_expense_amt', 'fy_end_expense_amt'],
    extra=1,
    can_delete=True
)


class FundReceiptExpenseForm(forms.ModelForm):

    class Meta:
        model = FundReceiptExpense
        fields = '__all__'
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
            Row(
                Column('fiscal_year_from', css_class='col-md-3 mb-0'),
                Column('fy_month_from', css_class='col-md-3 mb-0'),
                Column('fiscal_year_to', css_class='col-md-3 mb-0'),
                Column('fy_month_to', css_class='col-md-3 mb-0'),
                css_class='form-row'
            ),
            Div(
                Fieldset('',
                    Formset('lines')
                ),
            )
        )