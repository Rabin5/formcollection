from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models.covidhospitaldetail import CovidHospitalDetail, CovidHospitalDetailLine


class CovidHospitalDetailLineForm(forms.ModelForm):

    class Meta:
        model = CovidHospitalDetailLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


CovidHospitaldetatilFormSet = inlineformset_factory(
    CovidHospitalDetail, CovidHospitalDetailLine, form=CovidHospitalDetailLineForm,
    fields=['covidhospital', 'announce_time_health_workers', 'announce_time_beds',
            'announce_time_icu', 'announce_time_ventilators', 'added_health_workers', 'added_beds', 'added_icu', 'added_ventilators', 'num_treated_patients', 'expense_treatment'],
    widgets={

    },
    extra=1,
    can_delete=False
)


class CovidHospitalDetailForm(forms.ModelForm):

    class Meta:
        model = CovidHospitalDetail
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
