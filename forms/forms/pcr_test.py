from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models.pcr_test_compliance_detail import PcrTestComplianceDetail, PcrTestComplianceDetailLine


class PcrTestForm(forms.ModelForm):

    class Meta:
        model = PcrTestComplianceDetailLine
        exclude = ()


PcrTestFormSet = inlineformset_factory(
    PcrTestComplianceDetail, PcrTestComplianceDetailLine, form=PcrTestForm,
    fields=['month', 'year', 'all_area_test_num',
            'all_area_infected_num', 'priority_1_test_num', 'priority_1_infected_num', 'priority_2_test_num', 'priority_2_infected_num',
            'priority_3_test_num', 'priority_3_infected_num', 'non_priority_test_num', 'non_priority_infected_num'],
    extra=1,
    can_delete=True
)


class PcrTestFormLine(forms.ModelForm):

    class Meta:
        model = PcrTestComplianceDetail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('body'),
                Field('fiscal_year'),
                Fieldset('Add lines. . .',
                         Formset('lines')
                         ),
                HTML('<br>'),
                ButtonHolder(Submit('submit', 'save')),
            )
        )
