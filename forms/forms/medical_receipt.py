from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit

from forms.custom_layout_object import Formset
from forms.models.medical_receipt import MedicalReceiptLine, MedicalReceipt


class MedicalReceiptLineForm(forms.ModelForm):

    class Meta:
        model = MedicalReceiptLine
        exclude = ()


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('body'),
                Field('fiscal_year'),
                Fieldset('Add lines. . .',
                         Formset('lines')
                         ),
                HTML('<br>'),
                ButtonHolder(Submit('submit', 'save')),
            )
        )
