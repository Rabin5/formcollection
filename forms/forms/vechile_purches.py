from django import forms
from django.forms.forms import Form
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.vechile_purches import VehiclePurchase, VehiclePurchaseLine
from master_data.models.vehicle import Vehicle


class VehiclePurchaseForm(forms.ModelForm):
    vehicle = ModelChoiceFieldWithCreate(queryset=Vehicle.objects.all(
    ), label='सवारी साधन', blank=False, save_to_field='name')

    class Meta:
        model = VehiclePurchaseLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


VehiclePurchaseFormSet = inlineformset_factory(
    VehiclePurchase, VehiclePurchaseLine, form=VehiclePurchaseForm,
    fields=['vehicle', 'purchased_amount', 'price', 'body',
            'remarks'],
    widgets={

    },
    extra=1,
    can_delete=True
)


class VehiclePurchaseFormLine(forms.ModelForm):

    class Meta:
        model = VehiclePurchase
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
                Fieldset('', Formset('lines')
                         ),
            )
        )
