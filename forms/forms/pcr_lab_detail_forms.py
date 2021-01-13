from django import forms
from django.db.models import fields
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

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
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


PcrLaboratoryDetailLineFormSet = inlineformset_factory(
    PcrLaboratoryDetail, PcrLaboratoryDetailLine, form=PcrLaboratoryDetailLineForm,
    fields=['pcr_lab_detail', 'laboratory', 'date_establishment', 'capacity_daily_test', 'num_tested_fy_end', 'num_infected', 'time_test_result', 'expense_pcr_test'],
    # widgets = {
    #     'date_establishment': NepaliDateInput(),
    # },
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
            Div(
                Fieldset('',
                    Formset('lines')
                ),
            )
        )
