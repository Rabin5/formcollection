from django import forms
from forms.models.case_investigation_tracing import CaseInvestigationTracing, CaseInvestigationTracingLine
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from forms.custom_layout_object import Formset
from crispy_forms.layout import Layout, Field, Fieldset, Div, ButtonHolder, Submit, Hidden, Row, Column


class CaseInvestigationLineForm(forms.ModelForm):
    class Meta:
        model = CaseInvestigationTracingLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


CaseInvestigationTracingFormSet = inlineformset_factory(CaseInvestigationTracing, CaseInvestigationTracingLine, form=CaseInvestigationLineForm, fields=[
                                                        'description', 'num_team_members', 'amount_expense', 'num_searched_cases', 'num_identified_infection', 'remarks'], extra=1, can_delete=False)



class CaseInvestigationTracingForm(forms.ModelForm):
    class Meta:
        model = CaseInvestigationTracing
        exclude = ('create_user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.form_id = 'form_to_submit'
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-md-3 create-label'
        # self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Hidden('next_state', 'next'),
            Row(Column('body', css_class='col-md-6 mb-0'),
                Column('fiscal_year', css_class='col-md-6 mb-0'),
                css_class='form-row'
                ),
            Div(Fieldset('', Formset('lines')),

                )

        )
