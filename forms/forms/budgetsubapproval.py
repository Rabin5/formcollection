from django import forms
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit
from forms.custom_layout_object import Formset
from forms.models.budgetsubapproval import BudgetSubmitApproval, BudgetSubmitApprovalLine


class BudgetSubmitApprovalForm(forms.ModelForm):
    class Meta:
        model = BudgetSubmitApprovalLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


BudgetSubmitApprovalFormSet = inlineformset_factory(
    BudgetSubmitApproval, BudgetSubmitApprovalLine, form=BudgetSubmitApprovalForm,
    fields=['desc', 'date', 'total_budget',
            'amount', 'budgetsubmitapproval_line'],
    extra=1,
    can_delete=True
)


class BudgetSubmitApprovalFormLine(forms.ModelForm):

    class Meta:
        model = BudgetSubmitApproval
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
                Fieldset('',
                         Formset('lines')
                         ),
            )
        )
