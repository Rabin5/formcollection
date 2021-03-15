from django import forms
from django.forms.models import inlineformset_factory

import nepali_datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from master_data.widgets import NepaliDateInput
from forms.models.program_monitoring import ProgramMonitoring, ProgramMonitoringLine


class ProgramMonitoringLineForm(forms.ModelForm):

    class Meta:
        model = ProgramMonitoringLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    

ProgramMonitoringLineFormSet = inlineformset_factory(
    ProgramMonitoring, ProgramMonitoringLine, form=ProgramMonitoringLineForm,
    fields=['fiscal_year', 'program_name', 'follow_up_date', 
    'monitoring_body', 'behaviour', 'program_monitoring_line'],
    extra=1,
    can_delete=True,
    widgets = {
        'follow_up_date': NepaliDateInput(),
    },
)


class ProgramMonitoringForm(forms.ModelForm):

    class Meta:
        model = ProgramMonitoring
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
