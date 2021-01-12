from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models import MedicalPurchaseDescription, MedicalPurchaseDescriptionLine
from master_data.widgets import NepaliDateInput

class MedPurchaseDescLineForm(forms.ModelForm):

    class Meta:
        model = MedicalPurchaseDescriptionLine
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


MedPurchaseDescLineFormSet = inlineformset_factory(
    MedicalPurchaseDescription, MedicalPurchaseDescriptionLine, form=MedPurchaseDescLineForm,
    fields=['medical_purchase', 'product', 'uom', 'product_specificaiton', 'date_procure_agreement', 'date_received', 'qty', 'rate', 'total_amt'],
    widgets = {
        'date_procure_agreement': NepaliDateInput(),
        'date_received': NepaliDateInput(),
    },
    extra=1,
    can_delete=False
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
            Div(
                Fieldset('',
                    Formset('lines')
                ),
            )
        )
