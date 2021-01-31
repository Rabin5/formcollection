from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.models import MedicalPurchaseDescription, MedicalPurchaseDescriptionLine
from master_data.widgets import NepaliDateInput

class MedPurchaseDescLineForm(forms.ModelForm):

    class Meta:
        model = MedicalPurchaseDescriptionLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


MedPurchaseDescLineFormSet = inlineformset_factory(
    MedicalPurchaseDescription, MedicalPurchaseDescriptionLine, form=MedPurchaseDescLineForm,
    fields=['medical_purchase', 'product','product_specificaiton', 'date_procure_agreement', 'date_received', 'uom', 'qty', 'rate', 'total_amt'],
    widgets = {
        'date_procure_agreement': NepaliDateInput(),
        'date_received': NepaliDateInput(),
    },
    extra=1,
    can_delete=True
)


class MedPurchaseDescForm(forms.ModelForm):

    class Meta:
        model = MedicalPurchaseDescription
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
