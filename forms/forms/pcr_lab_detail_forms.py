from django import forms
from django.db.models import fields
from django.forms.fields import ChoiceField
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.models import PcrLaboratoryDetail, PcrLaboratoryDetailLine
from master_data import widgets
from master_data.widgets import NepaliDateInput

class PcrLaboratoryDetailLineForm(forms.ModelForm):
    date_establishment = forms.CharField(max_length=15, label='स्थापना मिति', widget=NepaliDateInput())
    capacity_daily_test = forms.IntegerField(label='दैनिक परीक्षण क्षमता')

    class Meta:
        model = PcrLaboratoryDetailLine
        exclude = ()
        
        # fields = 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            if field.widget.input_type == 'select':
                field.widget.attrs.update({'class': 'select_class', 'onchange': 'get_select_value(event)'})
                # field.widget.attrs.update({'class': 'select_class'})
            else:
                field.widget.attrs['class'] = 'form-control'
        

PcrLaboratoryDetailLineFormSet = inlineformset_factory(
    PcrLaboratoryDetail, PcrLaboratoryDetailLine, form=PcrLaboratoryDetailLineForm,
    fields=['pcr_lab_detail', 'laboratory', 'date_establishment', 'capacity_daily_test', 'num_tested_fy_end', 'num_infected', 'time_test_result', 'expense_pcr_test'],
    widgets = {
        # 'laboratory': forms.ChoiceField(choices=get_lab_val()),
    },
    extra=1,
    can_delete=False
)


class PcrLaboratoryDetailForm(forms.ModelForm):

    class Meta:
        model = PcrLaboratoryDetail
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
