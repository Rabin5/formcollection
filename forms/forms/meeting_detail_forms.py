from django import forms
from django.forms.models import inlineformset_factory

import nepali_datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from master_data.widgets import NepaliDateInput
from forms.models.meeting_detail import MeetingDetail, MeetingDetailLine


class MeetingDetailLineForm(forms.ModelForm):

    class Meta:
        model = MeetingDetailLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    

MeetingDetailLineFormSet = inlineformset_factory(
    MeetingDetail, MeetingDetailLine, form=MeetingDetailLineForm,
    fields=['fiscal_year', 'meeting_date', 'meeting_conclusion', 
    'meeting_detail_line'],
    extra=1,
    can_delete=True,
    widgets = {
        'meeting_date': NepaliDateInput(),
    },
)


class MeetingDetailForm(forms.ModelForm):

    class Meta:
        model = MeetingDetail
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
