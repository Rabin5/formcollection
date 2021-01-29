from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.models.pcr_test_compliance_detail import PcrTestComplianceDetail, PcrTestComplianceDetailLine


class PcrTestLineForm(forms.ModelForm):

    class Meta:
        model = PcrTestComplianceDetailLine
        exclude = ()
        widgets = {
            'year': forms.TextInput()
        }
    
    def clean_year(self):
        year = self.cleaned_data.get('year')
        if 2076 <= year <= 2080:
            return year
        raise forms.ValidationError('Invalid year.')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


PcrTestFormSet = inlineformset_factory(
    PcrTestComplianceDetail, PcrTestComplianceDetailLine, form=PcrTestLineForm,
    fields=['month', 'year', 'all_area_test_num',
            'all_area_infected_num', 'priority_1_test_num', 'priority_1_infected_num', 'priority_2_test_num', 'priority_2_infected_num',
            'priority_3_test_num', 'priority_3_infected_num', 'non_priority_test_num', 'non_priority_infected_num'],
    extra=1,
    can_delete=False
)


class PcrTestForm(forms.ModelForm):

    class Meta:
        model = PcrTestComplianceDetail
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
            )
        )