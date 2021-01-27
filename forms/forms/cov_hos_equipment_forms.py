from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.models import CovidHospitalEquipment, CovidHospitalEquipmentLine

class CovidHospitalEquipmentLineForm(forms.ModelForm):

    class Meta:
        model = CovidHospitalEquipmentLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


CovidHospitalEquipmentLineFormSet = inlineformset_factory(
    CovidHospitalEquipment, CovidHospitalEquipmentLine, form=CovidHospitalEquipmentLineForm,
    fields=['cov_hos_equip', 'product', 'num_required', 'available', 'num_still_required'],
    widgets = {

    },
    extra=1,
    can_delete=False
)


class CovidHospitalEquipmentForm(forms.ModelForm):

    class Meta:
        model = CovidHospitalEquipment
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
                Column('cov_hospital', css_class='col-md-6 mb-0'),
                css_class='form-row'
                ),
            Div(
                Fieldset('',
                    Formset('lines')
                ),
            )

        )
