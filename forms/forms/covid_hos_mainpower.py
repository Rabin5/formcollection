from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models import CovidHospitalManpower, CovidHospitalManpowerLine, Manpower


class CovidHospitalManpowerLineForm(forms.ModelForm):
    manpower = ModelChoiceFieldWithCreate(queryset=Manpower.objects.all(), label='स्वास्थ्य जनशक्ति', blank=False, save_to_field='title')
    class Meta:
        model = CovidHospitalManpowerLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


CovidHospitalmainpowerFormSet = inlineformset_factory(
    CovidHospitalManpower, CovidHospitalManpowerLine, form=CovidHospitalManpowerLineForm,
    fields=['manpower', 'num_required', 'num_hired',
            'num_vacant', 'num_contract'],
    widgets={

    },
    extra=1,
    can_delete=True
)


class CovidHospitalManpowerForm(forms.ModelForm):

    class Meta:
        model = CovidHospitalManpower
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
                Column('covidhospital', css_class='col-md-6 mb-0'),
                css_class='form-row'
            ),
            Div(
                Fieldset('',
                         Formset('lines')
                         ),
            )

        )
