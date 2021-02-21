from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models import CovidHospitalEquipment, CovidHospitalEquipmentLine, Product

class CovidHospitalEquipmentLineForm(forms.ModelForm):
    product = ModelChoiceFieldWithCreate(queryset=Product.objects.all(), label='स्वास्थ्य उपकरण', blank=False, save_to_field='name')

    class Meta:
        model = CovidHospitalEquipmentLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


CovidHospitalEquipmentLineFormSet = inlineformset_factory(
    CovidHospitalEquipment, CovidHospitalEquipmentLine, form=CovidHospitalEquipmentLineForm,
    fields=['cov_hos_equip', 'product', 'num_required', 'available', 'num_still_required'],
    widgets = {

    },
    extra=1,
    can_delete=True
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
