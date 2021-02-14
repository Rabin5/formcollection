from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Row, Column, Hidden

from forms.custom_layout_object import Formset
from forms.fields import ModelChoiceFieldWithCreate
from forms.models.medical_receipt import MedicalReceiptLine, MedicalReceipt, Institution, Product


class MedicalReceiptLineForm(forms.ModelForm):
    product = ModelChoiceFieldWithCreate(queryset=Product.objects.all(), blank=False, label='स्वास्थ्य सामाग्री उपकरण', save_to_field='name')
    provider_institution = ModelChoiceFieldWithCreate(queryset=Institution.objects.all(), label='यदि संस्था भए, प्रदान गर्ने संस्था', save_to_field='name')

    class Meta:
        model = MedicalReceiptLine
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


MedicalReceiptFormSet = inlineformset_factory(
    MedicalReceipt, MedicalReceiptLine, form=MedicalReceiptLineForm,
    fields=['product', 'provider_institution', 'provider_body',
            'quantity', 'cost_received_items', 'usage_situation'],
    extra=1,
    can_delete=True
)


class MedicalReceiptForm(forms.ModelForm):

    class Meta:
        model = MedicalReceipt
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