from django import forms
from django.forms.forms import Form
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.admin_operative_expense import AdminOperativeExpense, AdminOperativeExpenseLine


class AdminOperativeExpenseLineForm(forms.ModelForm):
    
    class Meta:
        model = AdminOperativeExpenseLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    

AdminOperativeExpenseLineFormSet = inlineformset_factory(
    AdminOperativeExpense, AdminOperativeExpenseLine, form=AdminOperativeExpenseLineForm,
    fields=['designation', 'monthly_salary_expense', 'total_expense_pre_previous_fy',
            'total_expense_previous_fy', 'total_expense_current_fy',
            'admin_op_expense_line'],
    extra=1,
    can_delete=False
)


class AdminOperativeExpenseForm(forms.ModelForm):

    class Meta:
        model = AdminOperativeExpense
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
                css_class='form-row'
            ),
            Div(
                Fieldset('', Formset('lines')
                         ),
                Column('amt_operational_expenses', css_class='col-md-6 mb-0'),
                # ButtonHolder(Submit('submit', 'save')),
            )
        )
