from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models.case_inve_trac_operations import CaseInvestigationTracingOperationsLine, CaseInvestigationTracingOperations


class CaseInvestigationTracingOptLineForm(forms.ModelForm):

    class Meta:
        model = CaseInvestigationTracingOperationsLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


CaseInvestigationTracingOptFormSet = inlineformset_factory(
    CaseInvestigationTracingOperations, CaseInvestigationTracingOperationsLine, form=CaseInvestigationTracingOptLineForm,
    fields=['case_invs_body', 'num_team_members', 'amt_expense',
            'num_case', 'num_contact_identified', 'num_consult_refer', 'num_sample_collect_test',
            'caseinvestigationtracingoperations_line'],
    widgets={

    },
    extra=1,
    can_delete=True
)


class CaseInvestigationTracingOptForm(forms.ModelForm):

    class Meta:
        model = CaseInvestigationTracingOperations
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
            Div(
                Fieldset('',
                         Formset('lines')
                         ),
                # ButtonHolder(Submit('submit', 'save')),
            )

        )
